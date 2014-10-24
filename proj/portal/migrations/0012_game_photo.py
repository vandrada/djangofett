# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_remove_game_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='photo',
            field=models.ImageField(default=b'https://upload.wikimedia.org/wikipedia/commons/7/7a/Japan_road_sign_302.svg', upload_to=b'games'),
            preserve_default=True,
        ),
    ]
