# Generated by Django 4.2.2 on 2023-07-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0029_character_temp_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_spells', to='sheet.spell'),
        ),
    ]
