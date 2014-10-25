# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_game_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='photo',
        ),
    ]
