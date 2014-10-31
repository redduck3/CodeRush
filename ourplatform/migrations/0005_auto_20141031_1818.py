# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0004_auto_20141031_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endtime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='starttime',
            field=models.DateField(),
        ),
    ]
