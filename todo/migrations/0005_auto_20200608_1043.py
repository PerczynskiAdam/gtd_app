# Generated by Django 3.0.6 on 2020-06-08 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200605_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 10, 43, 5, 369349), verbose_name='date published'),
        ),
    ]
