# Generated by Django 4.2.2 on 2023-07-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0012_remove_character_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
