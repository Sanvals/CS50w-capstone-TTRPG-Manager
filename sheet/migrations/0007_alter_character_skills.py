# Generated by Django 4.2.2 on 2023-07-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0006_alter_character_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
