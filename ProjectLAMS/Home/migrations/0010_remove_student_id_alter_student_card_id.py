# Generated by Django 4.2.4 on 2023-10-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_student_id_alter_student_card_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='card_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
