# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20141022_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
    ]
