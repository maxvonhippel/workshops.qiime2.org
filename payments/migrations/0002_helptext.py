# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billed_datetime',
            field=models.DateTimeField(help_text='This is the confirmed date and time of payment', null=True, verbose_name='billed date & time'),
        ),
        migrations.AlterField(
            model_name='order',
            name='billed_total',
            field=models.DecimalField(decimal_places=2, help_text='This is the confirmed paid amount from NAU', max_digits=7, null=True, verbose_name='billed total (USD)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='order total (USD)'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='price (USD)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='slug',
            field=models.SlugField(help_text='This is the unique identifier for the URL (i.e. title-YYYY-MM-DD)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='url',
            field=models.URLField(max_length=2000, verbose_name='URL'),
        ),
    ]
