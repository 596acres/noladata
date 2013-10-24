from django.contrib.gis.db import models


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
    objects = models.GeoManager()


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
