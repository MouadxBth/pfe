# Generated by Django 4.1.6 on 2023-04-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agence', '0030_remove_offer_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]