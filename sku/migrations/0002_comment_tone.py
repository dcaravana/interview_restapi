# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sku', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tone',
            field=models.TextField(blank=True),
        ),
    ]
