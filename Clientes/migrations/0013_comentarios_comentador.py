# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 23:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clientes', '0012_delete_administradores'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='comentador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentador', to=settings.AUTH_USER_MODEL),
        ),
    ]
