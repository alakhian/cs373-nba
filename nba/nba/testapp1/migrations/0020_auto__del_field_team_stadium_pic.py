# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Team.stadium_pic'
        db.delete_column('testapp1_team', 'stadium_pic')


    def backwards(self, orm):
        # Adding field 'Team.stadium_pic'
        db.add_column('testapp1_team', 'stadium_pic',
                      self.gf('django.db.models.fields.URLField')(default='', unique=True, max_length=200),
                      keep_default=False)


    models = {
        'testapp1.player': {
            'Meta': {'object_name': 'Player'},
            'alldef_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'allnba_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'ast': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'blk': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'current_team': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'related_name': "'current_team'", 'to_field': "'name'", 'to': "orm['testapp1.Team']"}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fgperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'finals_teams': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'finals_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'finalsmvp_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'ftperc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'gp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.URLField', [], {'default': "''", 'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minpg': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'mvp_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'photo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'pts': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reb': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'stl': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'years_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'testapp1.team': {
            'Meta': {'object_name': 'Team'},
            'coach': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'finals_mvps': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'finals_years': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'gm': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'map_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'map_lat': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'map_lng': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'mvps': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stadium': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'twitter': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'twitter_widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'})
        },
        'testapp1.year': {
            'Meta': {'object_name': 'Year'},
            'all_def': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'all_nba': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'related_name': "'champion'", 'to_field': "'name'", 'to': "orm['testapp1.Team']"}),
            'finals_logo': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'finals_mvp': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'related_name': "'finals_mvp'", 'to_field': "'name'", 'to': "orm['testapp1.Player']"}),
            'finals_recap': ('django.db.models.fields.TextField', [], {}),
            'highlights': ('django.db.models.fields.URLField', [], {'default': "''", 'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg_mvp': ('django.db.models.fields.related.ForeignKey', [], {'default': "'none'", 'related_name': "'reg_mvp'", 'to_field': "'name'", 'to': "orm['testapp1.Player']"}),
            'year': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['testapp1']