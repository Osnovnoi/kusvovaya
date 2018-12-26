# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Step1', '0003_auto_20181212_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='RoomId',
            field=models.ForeignKey(default=0, to='Step1.Room'),
        ),
    ]
