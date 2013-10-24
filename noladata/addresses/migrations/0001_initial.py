# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'addresses_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('aid', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('addr_type', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('dir', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True)),
            ('address_la', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('x', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('y', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('house_alph', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('house_numb', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('streetid', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('parcel_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('geopin', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('buildid', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('in_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'addresses', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'addresses_address')


    models = {
        u'addresses.address': {
            'Meta': {'object_name': 'Address'},
            'addr_type': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'address_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address_la': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'aid': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'buildid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dir': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'geopin': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'house_alph': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'house_numb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parcel_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'streetid': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'y': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['addresses']