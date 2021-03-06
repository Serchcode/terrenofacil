# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0008_auto_20161109_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=140, null=True)),
                ('correo', models.EmailField(blank=True, max_length=140, null=True)),
                ('username', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('coment', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Clientes.Cliente')),
            ],
            options={
                'ordering': ('-fecha',),
            },
        ),
    ]
