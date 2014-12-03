# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0024_reviewresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
