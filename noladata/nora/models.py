from django.contrib.gis.db import models


class UncommittedProperty(models.Model):
    """
    An uncommitted property in New Orleans held by NORA (the New Orleans
    Redevelopment Authority) as defined and listed in the following file:

        https://data.nola.gov/Administrative-Data/NORA-Uncommitted-Property-Inventory/5ktx-e9wc

    """
    identifier = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    property_address = models.CharField(
        max_length=100,
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    state = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )
    zip = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    geom = models.PointField()
    objects = models.GeoManager()
