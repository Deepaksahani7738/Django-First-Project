# Generated by Django 4.1.7 on 2023-02-26 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
