# Generated by Django 4.2.4 on 2023-10-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_time_remove_log_id_remove_log_ida_remove_log_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Time',
        ),
        migrations.RemoveField(
            model_name='log',
            name='all_total',
        ),
        migrations.AddField(
            model_name='student',
            name='time_spend',
            field=models.CharField(default='total time spend', max_length=50),
        ),
    ]
