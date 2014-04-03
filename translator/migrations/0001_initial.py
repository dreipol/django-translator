# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Translation'
        db.create_table(u'translator_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'translator', ['Translation'])


    def backwards(self, orm):
        # Deleting model 'Translation'
        db.delete_table(u'translator_translation')


    models = {
        u'translator.translation': {
            'Meta': {'object_name': 'Translation'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['translator']