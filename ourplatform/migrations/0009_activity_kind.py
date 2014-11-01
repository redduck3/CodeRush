# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourplatform', '0008_auto_20141031_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='kind',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
