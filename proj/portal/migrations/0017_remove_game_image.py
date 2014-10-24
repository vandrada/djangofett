# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_auto_20141024_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
    ]
