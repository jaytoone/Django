# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 21:41
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calcmain', '0003_studyanalysis_reassessed_df'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyanalysis',
            name='sorted_df',
            field=picklefield.fields.PickledObjectField(default='None', editable=False),
        ),
    ]
