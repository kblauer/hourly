# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedentry', '0003_auto_20150324_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleentry',
            name='allDay',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
