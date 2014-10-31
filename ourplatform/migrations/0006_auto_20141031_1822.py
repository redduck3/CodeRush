# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0005_auto_20141031_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joiner',
            old_name='username',
            new_name='user',
        ),
    ]
