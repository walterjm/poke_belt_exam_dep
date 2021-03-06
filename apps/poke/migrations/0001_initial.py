# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokeamount', to='poke.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='poking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poketake', to='poke.User'),
        ),
    ]
