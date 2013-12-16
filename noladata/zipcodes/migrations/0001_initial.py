# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ZipCode'
        db.create_table(u'zipcodes_zipcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('simplified_geometry', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('statefp10', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('geoid10', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('classfp10', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('mtfcc10', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('funcstat10', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('aland10', self.gf('django.db.models.fields.FloatField')()),
            ('awater10', self.gf('django.db.models.fields.FloatField')()),
            ('intptlat10', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('intptlon10', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('partflg10', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'zipcodes', ['ZipCode'])


    def backwards(self, orm):
        # Deleting model 'ZipCode'
        db.delete_table(u'zipcodes_zipcode')


    models = {
        u'zipcodes.zipcode': {
            'Meta': {'object_name': 'ZipCode'},
            'aland10': ('django.db.models.fields.FloatField', [], {}),
            'awater10': ('django.db.models.fields.FloatField', [], {}),
            'classfp10': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'funcstat10': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'geoid10': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat10': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'intptlon10': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'mtfcc10': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'partflg10': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'simplified_geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'statefp10': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['zipcodes']