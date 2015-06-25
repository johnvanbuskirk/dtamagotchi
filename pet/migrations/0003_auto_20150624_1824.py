# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_pet_alive'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2015, 6, 25, 1, 24, 7, 693826, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 6, 25, 1, 24, 20, 189905, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
    ]
