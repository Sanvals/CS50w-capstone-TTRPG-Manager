# Generated by Django 4.2.2 on 2023-07-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0018_item_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
