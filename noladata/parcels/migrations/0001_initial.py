# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parcel'
        db.create_table(u'parcels_parcel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid_1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('perimeter', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('acres', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('hectares', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geopin', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('in_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('situs_dir', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('situs_stre', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('situs_type', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('situs_numb', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('situs_st_1', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('situs_stat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_len', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'parcels', ['Parcel'])


    def backwards(self, orm):
        # Deleting model 'Parcel'
        db.delete_table(u'parcels_parcel')


    models = {
        u'parcels.parcel': {
            'Meta': {'object_name': 'Parcel'},
            'acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'geopin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hectares': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'objectid_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_len': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'situs_dir': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'situs_numb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'situs_st_1': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'situs_stat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'situs_stre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'situs_type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['parcels']