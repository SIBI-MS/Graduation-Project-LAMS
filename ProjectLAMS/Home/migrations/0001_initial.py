# Generated by Django 2.2.2 on 2019-07-13 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id',models.AutoField(primary_key=True)),
                ('ida', models.IntegerField(default=0)),
                ('card_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2019, 7, 13, 22, 9, 30, 113365))),
                ('time_in', models.TimeField(default=datetime.datetime(2019, 7, 13, 22, 9, 30, 113365))),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('total_hours', models.CharField(max_length=50)),
                ('status', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('department', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=7, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
