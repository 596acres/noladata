# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZoningDistrict'
        db.create_table(u'zoning_zoningdistrict', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('zoneclass', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('zonedesc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('zonenum', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('zoneyear', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('ordnum', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('draftzone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('futlanduse', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('zoneclass1', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('zonenum1', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('zoneyear1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ordnum1', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('hyperlink', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('lasteditor', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('lastupdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dz_desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('dz_link', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('flu_desc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('flu_link', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_len', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'zoning', ['ZoningDistrict'])


    def backwards(self, orm):
        # Deleting model 'ZoningDistrict'
        db.delete_table(u'zoning_zoningdistrict')


    models = {
        u'zoning.zoningdistrict': {
            'Meta': {'object_name': 'ZoningDistrict'},
            'draftzone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'dz_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dz_link': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'flu_desc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flu_link': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'futlanduse': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'hyperlink': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'lasteditor': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'lastupdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ordnum': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ordnum1': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'zoneclass': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'zoneclass1': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'zonedesc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zonenum': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'zonenum1': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'zoneyear': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'zoneyear1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['zoning']