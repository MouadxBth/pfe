# Generated by Django 4.1.7 on 2023-03-28 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0014_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postulation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='log',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='postulation',
            name='candidate',
        ),
    ]