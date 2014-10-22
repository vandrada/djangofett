# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=100)),
                ('releaseDate', models.DateTimeField(verbose_name=b"Game's release date")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
