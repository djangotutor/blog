# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
