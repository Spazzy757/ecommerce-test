# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_price',
            field=models.DecimalField(max_digits=100, null=True, blank=True, default=6.99, decimal_places=2),
        ),
    ]
