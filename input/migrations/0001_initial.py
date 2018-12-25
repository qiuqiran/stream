# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-08-28 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=64)),
                ('short', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating_num', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='mid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input.Movie_list'),
        ),
    ]
