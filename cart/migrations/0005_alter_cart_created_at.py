# Generated by Django 4.2.7 on 2023-11-29 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_merge_0002_initial_0003_alter_cart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 11, 29)),
        ),
    ]
