# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]
