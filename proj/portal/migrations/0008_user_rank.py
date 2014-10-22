# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_game_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(default=b'NB', max_length=2, choices=[(b'NB', b'Noob'), (b'SM', b'Samaritan'), (b'PR', b'Professional'), (b'GT', b'Greatest of all time')]),
            preserve_default=True,
        ),
    ]
