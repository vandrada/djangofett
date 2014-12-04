# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0025_auto_20141203_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, default='ava_placeholder.png', upload_to='avatars'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('NB', 'Noob'), ('SM', 'Samaritan'), ('PR', 'Professional'), ('GT', 'Greatest of all time')], max_length=30, default='NB'),
        ),
    ]
