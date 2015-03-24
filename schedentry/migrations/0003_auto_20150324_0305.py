# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20150324_0035'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedentry', '0002_auto_20150324_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('allDay', models.BooleanField(default=False)),
                ('schedule', models.ForeignKey(to='schedule.Schedule')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='scheduleevent',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='scheduleevent',
            name='user',
        ),
        migrations.DeleteModel(
            name='ScheduleEvent',
        ),
    ]
