# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CouncilDistrict'
        db.create_table(u'councildistricts_councildistrict', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')()),
            ('unit_area', self.gf('django.db.models.fields.FloatField')()),
            ('unit_perim', self.gf('django.db.models.fields.FloatField')()),
            ('shape_area', self.gf('django.db.models.fields.FloatField')()),
            ('shape_len', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'councildistricts', ['CouncilDistrict'])


    def backwards(self, orm):
        # Deleting model 'CouncilDistrict'
        db.delete_table(u'councildistricts_councildistrict')


    models = {
        u'councildistricts.councildistrict': {
            'Meta': {'object_name': 'CouncilDistrict'},
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_len': ('django.db.models.fields.FloatField', [], {}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'unit_area': ('django.db.models.fields.FloatField', [], {}),
            'unit_perim': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['councildistricts']