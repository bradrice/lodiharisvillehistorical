# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file_name', models.CharField(max_length=128)),
                ('file_title', models.CharField(max_length=256)),
                ('caption', models.TextField(max_length=1000)),
                ('sort_order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
