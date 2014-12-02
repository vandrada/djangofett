# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_user_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
