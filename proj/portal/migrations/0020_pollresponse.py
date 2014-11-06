# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20141106_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollResponse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('question', models.ForeignKey(to='portal.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
