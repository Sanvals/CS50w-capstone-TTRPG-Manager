# Generated by Django 4.2.2 on 2023-07-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_character_image_alter_character_charisma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.JSONField(default=dict),
        ),
    ]