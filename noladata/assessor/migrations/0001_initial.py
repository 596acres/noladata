# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParcelAssessorRecord'
        db.create_table(u'assessor_parcelassessorrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('owner_address', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('property_class', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_checked', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('parcel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.Parcel'])),
        ))
        db.send_create_signal(u'assessor', ['ParcelAssessorRecord'])


    def backwards(self, orm):
        # Deleting model 'ParcelAssessorRecord'
        db.delete_table(u'assessor_parcelassessorrecord')


    models = {
        u'assessor.parcelassessorrecord': {
            'Meta': {'object_name': 'ParcelAssessorRecord'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_checked': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner_address': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parcels.Parcel']"}),
            'property_class': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
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

    complete_apps = ['assessor']