# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-30 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_institucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='institucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Institucion'),
        ),
    ]
