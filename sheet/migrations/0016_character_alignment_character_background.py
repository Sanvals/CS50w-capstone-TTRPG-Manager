# Generated by Django 4.2.2 on 2023-07-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0015_character_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alignment',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='character',
            name='background',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
