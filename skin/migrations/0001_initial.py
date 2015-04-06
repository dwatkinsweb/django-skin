# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'SiteSkin'
        db.create_table(u'skin_siteskin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('path', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'skin', ['SiteSkin'])

        # Adding unique constraint on 'SiteSkin', fields ['site', 'name']
        db.create_unique(u'skin_siteskin', ['site_id', 'name'])

    def backwards(self, orm):
        # Removing unique constraint on 'SiteSkin', fields ['site', 'name']
        db.delete_unique(u'skin_siteskin', ['site_id', 'name'])

        # Deleting model 'SiteSkin'
        db.delete_table(u'skin_siteskin')

    models = {
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'skin.siteskin': {
            'Meta': {'unique_together': "((u'site', u'name'),)", 'object_name': 'SiteSkin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        }
    }

    complete_apps = ['skin']