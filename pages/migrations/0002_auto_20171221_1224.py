# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-21 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title_descriprion',
            new_name='title_description',
        ),
    ]
