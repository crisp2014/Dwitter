# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-29 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dweet',
        ),
        migrations.AddField(
            model_name='comment',
            name='dweet',
            field=models.ManyToManyField(null=True, to='accounts.Dweet'),
        ),
    ]
