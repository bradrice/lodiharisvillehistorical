# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='show_in_set',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='caption',
            field=models.TextField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
