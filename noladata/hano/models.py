from django.contrib.gis.db import models


class ScatteredSite(models.Model):
    """
    A "Scattered Site for Disposition" according to a HANO document.
    """
    address = models.CharField(
        max_length=100,
    )
    units = models.IntegerField(
        blank=True,
        null=True,
    )
