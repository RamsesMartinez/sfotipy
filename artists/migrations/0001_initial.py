# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('biography', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Artists',
                'verbose_name': 'Artist',
            },
        ),
    ]
