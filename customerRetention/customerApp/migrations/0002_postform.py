# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-02-11 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'Name',
                'managed': False,
            },
        ),
    ]
