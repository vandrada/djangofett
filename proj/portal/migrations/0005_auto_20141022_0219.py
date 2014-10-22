# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20141022_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField()),
                ('karma', models.IntegerField(default=0)),
                ('reported_count', models.IntegerField(default=0)),
                ('author_id', models.ForeignKey(to='portal.User')),
                ('game_id', models.ForeignKey(to='portal.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='karma',
        ),
    ]
