# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_list',
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
            preserve_default=False,
        ),
    ]
