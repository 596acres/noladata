from django.contrib.gis.db import models

from inplace.boundaries.models import BaseBoundary


class ZipCode(BaseBoundary):
    statefp10 = models.CharField(max_length=2)
    geoid10 = models.CharField(max_length=7)
    classfp10 = models.CharField(max_length=2)
    mtfcc10 = models.CharField(max_length=5)
    funcstat10 = models.CharField(max_length=1)
    aland10 = models.FloatField()
    awater10 = models.FloatField()
    intptlat10 = models.CharField(max_length=11)
    intptlon10 = models.CharField(max_length=12)
    partflg10 = models.CharField(max_length=1)


zipcode_mapping = {
    'statefp10' : 'STATEFP10',
    'label' : 'ZCTA5CE10',
    'geoid10' : 'GEOID10',
    'classfp10' : 'CLASSFP10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'partflg10' : 'PARTFLG10',
    'geometry' : 'POLYGON',
}
