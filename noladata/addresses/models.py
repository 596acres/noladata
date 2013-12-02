from django.contrib.gis.db import models


class Address(models.Model):
    """
    This is an auto-generated Django model module created by ogrinspect.

    A representation of an address in New Orleans as defined in the address
    shapefile released by the city:

        https://data.nola.gov/Geographic-Reference/NOLA-Addresses/div8-5v7i

    """
    objectid = models.IntegerField(null=True, blank=True)
    aid = models.CharField(max_length=254, null=True, blank=True)
    addr_type = models.CharField(max_length=4, null=True, blank=True)
    dir = models.CharField(max_length=4, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=8, null=True, blank=True)
    address_la = models.CharField(max_length=75, null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    house_alph = models.CharField(max_length=10, null=True, blank=True)
    house_numb = models.IntegerField(null=True, blank=True)
    address_id = models.IntegerField(null=True, blank=True)
    streetid = models.CharField(max_length=9, null=True, blank=True)
    parcel_id = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=25, null=True, blank=True)
    geopin = models.IntegerField(null=True, blank=True)
    buildid = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    in_date = models.DateField(null=True, blank=True)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()


# Auto-generated `LayerMapping` dictionary for Address model
address_mapping = {
    'objectid' : 'OBJECTID',
    'aid' : 'AID',
    'addr_type' : 'ADDR_TYPE',
    'dir' : 'DIR',
    'street' : 'STREET',
    'type' : 'TYPE',
    'address_la' : 'ADDRESS_LA',
    'x' : 'X',
    'y' : 'Y',
    'house_alph' : 'HOUSE_ALPH',
    'house_numb' : 'HOUSE_NUMB',
    'address_id' : 'ADDRESS_ID',
    'streetid' : 'STREETID',
    'parcel_id' : 'PARCEL_ID',
    'source' : 'SOURCE',
    'geopin' : 'GEOPIN',
    'buildid' : 'BUILDID',
    'status' : 'STATUS',
    'in_date' : 'IN_DATE',
    'geom' : 'POINT',
}
