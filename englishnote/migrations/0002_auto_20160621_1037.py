# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-21 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishnote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='sentence',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='translation',
            field=models.TextField(),
        ),
    ]
