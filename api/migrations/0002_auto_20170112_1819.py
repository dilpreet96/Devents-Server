# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserLogin',
        ),
        migrations.AlterModelTable(
            name='userlogin',
            table='userlogin',
        ),
    ]
