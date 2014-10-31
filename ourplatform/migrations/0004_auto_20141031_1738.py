# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0003_auto_20141031_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='endstime',
            new_name='endtime',
        ),
    ]
