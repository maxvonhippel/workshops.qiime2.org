# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_billed_total_charfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='draft',
            field=models.BooleanField(default=True, help_text='Draft workshops do not show up on the workshop list overview'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='sales_open',
            field=models.BooleanField(default=False, help_text='Closed workshops do not show up on the workshop list overview'),
        ),
    ]
