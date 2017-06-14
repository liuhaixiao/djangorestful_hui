# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_zixun_publish_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('category', models.TextField(default='')),
                ('isComment', models.BooleanField(default=False)),
                ('publish_time', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('picture_list', models.TextField(default='')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]