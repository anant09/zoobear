# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.BigIntegerField()),
                ('height', models.BigIntegerField()),
                ('width', models.BigIntegerField()),
                ('length', models.BigIntegerField()),
                ('location_from', models.CharField(max_length=200)),
                ('location_to', models.CharField(max_length=200)),
            ],
        ),
    ]
