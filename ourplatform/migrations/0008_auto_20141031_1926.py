# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0007_auto_20141031_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='discription',
            new_name='description',
        ),
    ]
