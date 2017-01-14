# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(default=' ', max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gcm', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
