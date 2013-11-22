# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParcelBuildingOverlap'
        db.create_table(u'parcels_parcelbuildingoverlap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parcel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.Parcel'])),
            ('percent_parcel_covered', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'parcels', ['ParcelBuildingOverlap'])

        # Adding model 'BuildingOverlap'
        db.create_table(u'parcels_buildingoverlap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['buildings.Building'])),
            ('parcel_building_overlap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parcels.ParcelBuildingOverlap'])),
            ('percent_building_within_parcel', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'parcels', ['BuildingOverlap'])


    def backwards(self, orm):
        # Deleting model 'ParcelBuildingOverlap'
        db.delete_table(u'parcels_parcelbuildingoverlap')

        # Deleting model 'BuildingOverlap'
        db.delete_table(u'parcels_buildingoverlap')


    models = {
        u'buildings.building': {
            'Meta': {'object_name': 'Building'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'geopin': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'parcels.buildingoverlap': {
            'Meta': {'object_name': 'BuildingOverlap'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['buildings.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcel_building_overlap': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parcels.ParcelBuildingOverlap']"}),
            'percent_building_within_parcel': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
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
        },
        u'parcels.parcelbuildingoverlap': {
            'Meta': {'object_name': 'ParcelBuildingOverlap'},
            'buildings': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['buildings.Building']", 'null': 'True', 'through': u"orm['parcels.BuildingOverlap']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parcels.Parcel']"}),
            'percent_parcel_covered': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['parcels']