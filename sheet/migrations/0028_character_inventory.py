# Generated by Django 4.2.2 on 2023-07-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0027_spell_cost_alter_spell_components'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ManyToManyField(blank=True, related_name='users_inventory', to='sheet.item'),
        ),
    ]
