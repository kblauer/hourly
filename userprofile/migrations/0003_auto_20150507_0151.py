# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='manager',
            field=models.ForeignKey(related_name='manager', default=None, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
