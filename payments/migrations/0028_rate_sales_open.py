# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0027_rename_rate_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='sales_open',
            field=models.BooleanField(default=True),
        ),
    ]