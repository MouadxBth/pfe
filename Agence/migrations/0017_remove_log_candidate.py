# Generated by Django 4.1.7 on 2023-03-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0016_log_candidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='candidate',
        ),
    ]