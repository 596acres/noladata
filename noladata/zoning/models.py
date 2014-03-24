from django.contrib.gis.db import models


class ZoningDistrict(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    zoneclass = models.CharField(max_length=8, null=True, blank=True)
    zonedesc = models.CharField(max_length=100, null=True, blank=True)
    zonenum = models.CharField(max_length=5, null=True, blank=True)
    zoneyear = models.CharField(max_length=4, null=True, blank=True)
    ordnum = models.CharField(max_length=10, null=True, blank=True)
    draftzone = models.CharField(max_length=15, null=True, blank=True)
    futlanduse = models.CharField(max_length=15, null=True, blank=True)
    zoneclass1 = models.CharField(max_length=254, null=True, blank=True)
    zonenum1 = models.CharField(max_length=254, null=True, blank=True)
    zoneyear1 = models.IntegerField(null=True, blank=True)
    ordnum1 = models.CharField(max_length=254, null=True, blank=True)
    hyperlink = models.CharField(max_length=254, null=True, blank=True)
    lasteditor = models.CharField(max_length=5, null=True, blank=True)
    lastupdate = models.DateField(null=True, blank=True)
    dz_desc = models.CharField(max_length=100, null=True, blank=True)
    dz_link = models.CharField(max_length=254, null=True, blank=True)
    flu_desc = models.CharField(max_length=100, null=True, blank=True)
    flu_link = models.CharField(max_length=254, null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    shape_len = models.FloatField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()


zoningdistrict_mapping = {
    'objectid' : 'OBJECTID',
    'zoneclass' : 'ZONECLASS',
    'zonedesc' : 'ZONEDESC',
    'zonenum' : 'ZONENUM',
    'zoneyear' : 'ZONEYEAR',
    'ordnum' : 'ORDNUM',
    'draftzone' : 'DRAFTZONE',
    'futlanduse' : 'FUTLANDUSE',
    'zoneclass1' : 'ZONECLASS1',
    'zonenum1' : 'ZONENUM1',
    'zoneyear1' : 'ZONEYEAR1',
    'ordnum1' : 'ORDNUM1',
    'hyperlink' : 'HYPERLINK',
    'lasteditor' : 'LASTEDITOR',
    'lastupdate' : 'LASTUPDATE',
    'dz_desc' : 'DZ_DESC',
    'dz_link' : 'DZ_LINK',
    'flu_desc' : 'FLU_DESC',
    'flu_link' : 'FLU_LINK',
    'shape_area' : 'Shape_area',
    'shape_len' : 'Shape_len',
    'geom' : 'POLYGON',
}
