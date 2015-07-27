# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decoherence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state1', models.CharField(max_length=127)),
                ('state2', models.CharField(max_length=127)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('decohered', models.CharField(max_length=127, blank=True)),
            ],
        ),
    ]
