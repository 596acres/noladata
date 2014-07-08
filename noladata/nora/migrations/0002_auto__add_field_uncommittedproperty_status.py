# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UncommittedProperty.status'
        db.add_column(u'nora_uncommittedproperty', 'status',
                      self.gf('django.db.models.fields.CharField')(default='current', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UncommittedProperty.status'
        db.delete_column(u'nora_uncommittedproperty', 'status')


    models = {
        u'nora.uncommittedproperty': {
            'Meta': {'object_name': 'UncommittedProperty'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'property_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'current'", 'max_length': '20'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nora']