# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Case'
        db.create_table(u'codeenforcement_case', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('geopin', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('geoaddress', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('caseid', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('caseno', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('o_c', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('stage', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('statdate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('keystatus', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('initinspection', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('initinspresult', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('prevhearingdate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('prevhearingresult', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('casefiled', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('lastupload', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'codeenforcement', ['Case'])


    def backwards(self, orm):
        # Deleting model 'Case'
        db.delete_table(u'codeenforcement_case')


    models = {
        u'codeenforcement.case': {
            'Meta': {'object_name': 'Case'},
            'casefiled': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'caseid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'caseno': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'geoaddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'geopin': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initinspection': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'initinspresult': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'keystatus': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lastupload': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'o_c': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'prevhearingdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'prevhearingresult': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'statdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['codeenforcement']