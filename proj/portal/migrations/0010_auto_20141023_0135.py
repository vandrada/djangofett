# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20141023_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default=b'https://upload.wikimedia.org/wikipedia/commons/7/7a/Japan_road_sign_302.svg', upload_to=b'images/', verbose_name=b'game image', blank=True),
        ),
    ]
