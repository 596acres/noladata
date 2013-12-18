from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class NeighborhoodGroup(BaseBoundary):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
