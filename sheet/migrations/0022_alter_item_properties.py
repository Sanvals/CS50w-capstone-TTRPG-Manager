# Generated by Django 4.2.2 on 2023-07-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0021_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='properties',
            field=models.CharField(max_length=200),
        ),
    ]
