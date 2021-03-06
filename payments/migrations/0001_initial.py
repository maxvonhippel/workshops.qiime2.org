# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('billed_total', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('billed_datetime', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('url', models.URLField(max_length=2000)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Workshop'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Rate'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='workshops',
            field=models.ManyToManyField(related_name='instructors', to='payments.Workshop'),
        ),
    ]
