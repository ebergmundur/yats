# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-29 06:51
from __future__ import unicode_literals

from yats.shortcuts import convert_sarch, clean_search_values

from django.db import migrations
from django.core.serializers.json import DjangoJSONEncoder

import json

def convertOldStyleSearch(apps, schema_editor):
    boards = apps.get_model('yats', 'boards')
    for board in boards.objects.all():
        if board.columns:
            columns = json.loads(board.columns)
            for column in columns:
                search = column['query']
                column['query'] = convert_sarch(clean_search_values(search))

            board.columns = json.dumps(columns, cls=DjangoJSONEncoder)
            board.save()

class Migration(migrations.Migration):

    dependencies = [
        ('yats', '0012_auto_20180829_0820'),
    ]

    operations = [
        migrations.RunPython(convertOldStyleSearch),
    ]
