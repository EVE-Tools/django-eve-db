# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eve_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invmetatype',
            name='type',
            field=models.OneToOneField(related_name='inventorymetatype_type_set', primary_key=True, serialize=False, to='eve_db.InvType'),
        ),
        migrations.AlterField(
            model_name='mapcelestialstatistic',
            name='celestial',
            field=models.OneToOneField(primary_key=True, serialize=False, to='eve_db.MapDenormalize'),
        ),
        migrations.AlterField(
            model_name='mapjump',
            name='origin_gate',
            field=models.OneToOneField(related_name='stargate_jump_origin_set', primary_key=True, serialize=False, to='eve_db.MapDenormalize'),
        ),
        migrations.AlterField(
            model_name='maplocationwormholeclass',
            name='location',
            field=models.OneToOneField(primary_key=True, serialize=False, to='eve_db.MapDenormalize'),
        ),
    ]
