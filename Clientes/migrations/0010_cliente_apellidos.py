# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-21 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0009_administradores_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
