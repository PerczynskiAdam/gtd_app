# Generated by Django 3.0.6 on 2020-05-29 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_text', models.TextField(verbose_name='Action')),
                ('act_comp', models.BooleanField(default=False, verbose_name='complete action')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_text', models.CharField(max_length=200, verbose_name='Case')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 5, 29, 9, 45, 41, 308713), verbose_name='date published')),
                ('comp_case', models.BooleanField(default=False, verbose_name='complete case')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_text', models.CharField(max_length=200, verbose_name='Result')),
            ],
        ),
    ]