# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-05 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PincodeSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=120)),
                ('code', models.CharField(blank=True, max_length=120)),
            ],
        ),
    ]
