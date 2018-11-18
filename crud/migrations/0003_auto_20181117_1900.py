# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20181115_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='dni',
            new_name='Apellido',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='firstname',
            new_name='DNI',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='fechanac',
            new_name='Fechanac',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='lastname',
            new_name='Nombre',
        ),
    ]
