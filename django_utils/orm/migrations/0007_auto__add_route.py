# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Route'
        db.create_table(u'orm_route', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.LineStringField')()),
            ('geom_dist', self.gf('django.contrib.gis.db.models.fields.LineStringField')(srid=900913, null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('origin_taz', self.gf('django.db.models.fields.FloatField')()),
            ('destination_taz', self.gf('django.db.models.fields.FloatField')()),
            ('travel_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('json_contents', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'orm', ['Route'])


    def backwards(self, orm):
        # Deleting model 'Route'
        db.delete_table(u'orm_route')


    models = {
        u'orm.origin': {
            'Meta': {'object_name': 'Origin'},
            'cnty': ('django.db.models.fields.FloatField', [], {}),
            'cnty_1': ('django.db.models.fields.FloatField', [], {}),
            'emp08': ('django.db.models.fields.FloatField', [], {}),
            'emp20': ('django.db.models.fields.FloatField', [], {}),
            'emp35': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'geom_dist': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '900913', 'null': 'True', 'blank': 'True'}),
            'hh08': ('django.db.models.fields.FloatField', [], {}),
            'hh20': ('django.db.models.fields.FloatField', [], {}),
            'hh35': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop08': ('django.db.models.fields.FloatField', [], {}),
            'pop20': ('django.db.models.fields.FloatField', [], {}),
            'pop35': ('django.db.models.fields.FloatField', [], {}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'taz_id': ('django.db.models.fields.FloatField', [], {}),
            'taz_id_1': ('django.db.models.fields.FloatField', [], {})
        },
        u'orm.route': {
            'Meta': {'object_name': 'Route'},
            'destination_taz': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.LineStringField', [], {}),
            'geom_dist': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '900913', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_contents': ('django.db.models.fields.TextField', [], {}),
            'origin_taz': ('django.db.models.fields.FloatField', [], {}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'travel_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'orm.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'absolute_pm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'city_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cnty': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cnty_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'county_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'district_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emp_08': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'emp_20': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'emp_35': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'freeway': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hh_08': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hh_20': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hh_35': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lanes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'location_dist': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '900913', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pems_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pop_08': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_20': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_35': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sensor_length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sensor_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'state_pm': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'taz_id': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'taz_id_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user_id_1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_id_2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_id_3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_id_4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orm']