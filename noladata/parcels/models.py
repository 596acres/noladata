from django.contrib.gis.db import models
from django.db.models import Q

from ..addresses.models import Address
from ..buildings.models import Building
from .util import format_street_address


class ParcelManager(models.GeoManager):

    def filter_by_address(self, address):
        addresses = Address.objects.filter(address_la__iexact=address)
        if not addresses.count():
            return self.none()
        query = Q()
        for address in addresses:
            query = query | Q(geom__contains=address.geom)
        return self.filter(query)


class BuildingOverlap(models.Model):
    building = models.ForeignKey('buildings.Building')
    parcel_building_overlap = models.ForeignKey('parcels.ParcelBuildingOverlap')
    percent_building_within_parcel = models.FloatField(default=0.0)


class ParcelBuildingOverlap(models.Model):
    """
    Track the places where parcels are overlapped by buildings.
    """
    parcel = models.ForeignKey('parcels.Parcel')
    buildings = models.ManyToManyField('buildings.Building',
        null=True,
        blank=True,
        through='BuildingOverlap',
    )
    percent_parcel_covered = models.FloatField(default=0.0)


class Parcel(models.Model):
    """
    This is an auto-generated Django model module created by ogrinspect.

    A representation of a parcel in New Orleans as defined in the parcel
    shapefile released by the city:

        https://data.nola.gov/Geographic-Reference/NOLA-Parcels/e962-egyh

    Could also be worth looking at the following API for more data around
    parcels:

        http://gis.nola.gov/arcgis/rest/services/Staging/

    """
    objectid_1 = models.IntegerField(null=True, blank=True)
    objectid = models.IntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    perimeter = models.FloatField(null=True, blank=True)
    acres = models.FloatField(null=True, blank=True)
    hectares = models.FloatField(null=True, blank=True)
    geopin = models.IntegerField(null=True, blank=True)
    in_date = models.DateField(null=True, blank=True)
    situs_dir = models.CharField(max_length=4, null=True, blank=True)
    situs_stre = models.CharField(max_length=50, null=True, blank=True)
    situs_type = models.CharField(max_length=8, null=True, blank=True)
    situs_numb = models.IntegerField(null=True, blank=True)
    situs_st_1 = models.CharField(max_length=9, null=True, blank=True)
    situs_stat = models.IntegerField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    shape_len = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = ParcelManager()

    def _address(self):
        return format_street_address(
            house_number=self.situs_numb,
            street_dir=self.situs_dir,
            street_name=self.situs_stre,
            street_type=self.situs_type,
        )
    address = property(_address)

    def calculate_area(self):
        try:
            return self.geom.transform(3452, clone=True).area
        except Exception:
            return 0

    def calculate_building_overlap(self):
        """
        Find out how much of the given parcel is covered by buildings according
        to the city's shapefiles.
        """
        srid = 3452
        total_intersect = 0
        parcel_geometry = self.geom
        parcel_geometry.transform(srid)
        parcel_building_overlap = ParcelBuildingOverlap(parcel=self)

        # For each building, calculate how much it overlaps with the given
        # parcel and add this to the total
        buildings = Building.objects.filter_by_parcel(self)
        for building in buildings:
            building_geometry = building.geom
            building_geometry.transform(srid)
            intersection = parcel_geometry.intersection(building_geometry)
            total_intersect += intersection.area
            building_overlap = BuildingOverlap(
                building=building,
                parcel_building_overlap=parcel_building_overlap,
                percent_building_within_parcel=(intersection.area / building_geometry.area) * 100,
            )
            building_overlap.save()

        # Calculate and save the total
        percent_parcel_covered = (total_intersect / parcel_geometry.area) * 100
        parcel_building_overlap.percent_parcel_covered = percent_parcel_covered
        parcel_building_overlap.save()
        return parcel_building_overlap

    def probably_is_vacant(self):
        """
        Determine whether this parcel is vacant or not based solely on the
        area of the parcel and the percentage of its geometry that is covered
        by building parcels.

        The formula used here was determined by plotting areas against
        percentage covered and finding a line that seems to separate vacant
        parcels from parcels that are not vacant based on visual inspection.
        """
        # Get overlap record. If overlap does not exist, calculate.
        if not self.parcelbuildingoverlap_set.count():
            parcel_building_overlap = self.calculate_building_overlap()
        else:
            parcel_building_overlap = self.parcelbuildingoverlap_set.all()[0]
        percent_overlap = parcel_building_overlap.percent_parcel_covered

        # If there are no buildings overlapping at all, probably vacant
        if percent_overlap == 0:
            return True

        # Else try to guess based on the area and overlap
        area = self.calculate_area()
        return area < ((-900 * percent_overlap) + 10000)


# Auto-generated `LayerMapping` dictionary for Parcel model
parcel_mapping = {
    'objectid_1' : 'OBJECTID_1',
    'objectid' : 'OBJECTID',
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'acres' : 'ACRES',
    'hectares' : 'HECTARES',
    'geopin' : 'GEOPIN',
    'in_date' : 'IN_DATE',
    'situs_dir' : 'SITUS_DIR',
    'situs_stre' : 'SITUS_STRE',
    'situs_type' : 'SITUS_TYPE',
    'situs_numb' : 'SITUS_NUMB',
    'situs_st_1' : 'SITUS_ST_1',
    'situs_stat' : 'SITUS_STAT',
    'shape_area' : 'SHAPE_area',
    'shape_len' : 'SHAPE_len',
    'geom' : 'MULTIPOLYGON',
}
