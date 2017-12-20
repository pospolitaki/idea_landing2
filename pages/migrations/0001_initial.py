# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-20 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('title_descriprion', models.TextField(blank=True, null=True)),
                ('title_btn', models.CharField(default='Join', max_length=50)),
                ('title_btn_url', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
