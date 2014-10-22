# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='releaseDate',
            new_name='release_date',
        ),
    ]
