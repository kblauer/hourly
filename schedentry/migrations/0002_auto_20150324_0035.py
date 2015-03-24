# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedentry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleevent',
            name='schedule',
            field=models.ForeignKey(to='schedule.Schedule'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scheduleevent',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
