# Generated by Django 4.1.6 on 2023-03-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0012_alter_log_candidate_alter_log_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='log',
            name='company',
        ),
        migrations.RemoveField(
            model_name='log',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='company',
        ),
        migrations.AlterUniqueTogether(
            name='postulation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='postulation',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='postulation',
            name='offer',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Postulation',
        ),
    ]
