# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-02 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='list_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]