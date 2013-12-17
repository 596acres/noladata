from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class CouncilDistrict(BaseBoundary):
    objectid = models.IntegerField()
    unit_area = models.FloatField()
    unit_perim = models.FloatField()
    shape_area = models.FloatField()
    shape_len = models.FloatField()


councildistrict_mapping = {
    'objectid' : 'OBJECTID',
    'unit_area' : 'UNIT_AREA',
    'unit_perim' : 'UNIT_PERIM',
    'label' : 'COUNCILDIS',
    'shape_area' : 'SHAPE_area',
    'shape_len' : 'SHAPE_len',
    'geometry' : 'POLYGON',
}
