# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('portal', '0005_auto_20141022_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField()),
                ('reported_count', models.IntegerField(default=0)),
                ('review_id', models.ForeignKey(to='portal.Review')),
                ('user_id', models.ForeignKey(to='portal.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(verbose_name="Game's release date"),
        ),
    ]
