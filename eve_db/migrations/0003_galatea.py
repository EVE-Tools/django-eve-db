# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eve_db', '0002_system_check_fixes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invcategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='invgroup',
            name='allow_manufacture',
        ),
        migrations.RemoveField(
            model_name='invgroup',
            name='allow_recycle',
        ),
        migrations.RemoveField(
            model_name='invgroup',
            name='description',
        ),
        migrations.RemoveField(
            model_name='invtype',
            name='chance_of_duplicating',
        ),
        migrations.RemoveField(
            model_name='invtype',
            name='group',
        ),
    ]
