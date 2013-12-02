import re

from django.contrib.gis.db import models
from django.db.models import Q


directions = {
    'north': 'n',
    'east': 'e',
    'south': 's',
    'west': 'w',
}


# Common street types found in the City of New Orleans' address shapefile
street_types = {
    'alley': 'aly',
    'avenue': 'ave',
    'boulevard': 'blvd',
    'court': 'ct',
    'drive': 'dr',
    'expressway': 'expy',
    'highway': 'hwy',
    'lane': 'ln',
    'parkway': 'pkwy',
    'place': 'pl',
    'plaza': 'plz',
    'road': 'rd',
    'street': 'st',
    'terrace': 'ter',
    'trace': 'trce',
    'trail': 'trl',
}


def get_potential_addresses(address):
    """
    Get permutations of as many potential addresses as we can make out of
    the given address.

    Permutations include the address with all punctuation removed, the
    address with directions abbreviated, and the address with street types
    abbreviated (as they are in the City of New Orleans' addresses
    shapefile).
    """
    addresses = set()
    addresses.add(address.lower())

    # Try removing punctuation from the address
    for address in list(addresses):
        addresses.add(re.subn('[^\s\w]', '', address)[0])

    #  Try abbreviating directions
    for address in list(addresses):
        abbreviated = address
        for direction, abbr in directions.items():
            abbreviated = re.subn(r'\b%s\b' % direction, abbr, abbreviated)[0]
        addresses.add(abbreviated)

    # Abbreviate street types
    for address in list(addresses):
        for street_type, abbr in street_types.items():
            abbreviated = re.subn(r'\b%s\b' % street_type, abbr, address)[0]
            addresses.add(abbreviated)

    return tuple(addresses)


class AddressManager(models.GeoManager):

    def filter_by_full_address_fuzzy(self, address):
        query = Q()
        for address in get_potential_addresses(address):
            query = query | Q(address_la__iexact=address)
        return self.filter(query)


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
    objects = AddressManager()


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
