# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSkin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='Skin Name', db_index=True)),
                ('path', models.CharField(default='',
                                          help_text='Enter the path to add to any existing paths template loaders '
                                                    'will look. The path used will be {base_dir}{skin_path}{'
                                                    'template_name}.',
                                          max_length=255, verbose_name='Path Prefix', blank=True)),
                ('site', models.ForeignKey(verbose_name='Site', to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='siteskin',
            unique_together=set([('site', 'name')]),
        ),
    ]
