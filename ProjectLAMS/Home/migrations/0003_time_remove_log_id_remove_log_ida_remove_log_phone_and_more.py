# Generated by Django 4.2.4 on 2023-10-03 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200504_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('all_total', models.CharField(default='total time spend', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='log',
            name='id',
        ),
        migrations.RemoveField(
            model_name='log',
            name='ida',
        ),
        migrations.RemoveField(
            model_name='log',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='log',
            name='admission_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='all_total',
            field=models.CharField(default='total time spend', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='admission_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='log',
            name='card_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default='gender', max_length=50),
        ),
    ]
