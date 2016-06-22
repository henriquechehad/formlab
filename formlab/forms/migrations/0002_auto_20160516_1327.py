# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import formlab.core.resources


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='is_deleted',
        ),
        migrations.AlterField(
            model_name='form',
            name='xlsform_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=formlab.core.resources.FileUploadPath('xlsforms'), verbose_name='XLSForm File'),
        ),
    ]
