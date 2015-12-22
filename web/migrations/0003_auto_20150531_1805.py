# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150307_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagegallery',
            options={'ordering': ['sort_order']},
        ),
    ]
