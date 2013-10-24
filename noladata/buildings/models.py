from django.contrib.gis.db import models


class BuildingManager(models.GeoManager):

    def filter_by_parcel(self, parcel):
        return self.filter(geom__intersects=parcel.geom)


class Building(models.Model):
    """
    This is an auto-generated Django model module created by ogrinspect.

    A representation of a building in New Orleans as defined in the building
    shapefile released by the city:

        https://data.nola.gov/Geographic-Reference/Building-Outlines/t3vb-bbwe

    """
    objectid = models.IntegerField(null=True, blank=True)
    geopin = models.FloatField(null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = BuildingManager()


# Auto-generated `LayerMapping` dictionary for Building model
building_mapping = {
    'objectid' : 'OBJECTID',
    'geopin' : 'GEOPIN',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}
