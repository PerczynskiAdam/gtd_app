# Generated by Django 3.0.6 on 2020-06-08 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20200608_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='pub_date',
        ),
    ]
