# Generated by Django 3.0.2 on 2020-03-05 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
