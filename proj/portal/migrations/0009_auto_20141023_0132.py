# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default=b'http://www.clker.com/cliparts/T/G/C/H/K/W/no-sign-md.png', upload_to=b'images/', verbose_name=b'game image', blank=True),
        ),
    ]
