# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0006_auto_20141031_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joiner',
            old_name='activityid',
            new_name='activity',
        ),
    ]
