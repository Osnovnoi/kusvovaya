# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Step1', '0002_auto_20181208_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='IdRoom',
            field=models.ForeignKey(default=0, to='Step1.Room'),
        ),
    ]
