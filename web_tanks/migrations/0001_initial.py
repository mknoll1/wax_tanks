# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaxTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('desired_temp', models.IntegerField(default=0)),
                ('sensor_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WaxTankReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.IntegerField(default=0)),
                ('heat_active', models.BooleanField(default=False)),
                ('wax_tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_tanks.WaxTank')),
            ],
        ),
    ]
