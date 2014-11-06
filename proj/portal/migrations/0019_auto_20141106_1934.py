# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0018_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to='games'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(default='NB', max_length=2, choices=[('NB', 'Noob'), ('SM', 'Samaritan'), ('PR', 'Professional'), ('GT', 'Greatest of all time')]),
        ),
    ]
