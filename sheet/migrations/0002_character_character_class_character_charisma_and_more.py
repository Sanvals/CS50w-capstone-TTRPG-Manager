# Generated by Django 4.2.2 on 2023-07-20 12:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_class',
            field=models.CharField(choices=[('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Monk', 'Monk'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Rogue', 'Rogue'), ('Sorcerer', 'Sorcerer'), ('Warlock', 'Warlock'), ('Wizard', 'Wizard')], default='Barbarian', max_length=20),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='charisma_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_player', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(choices=[('Human', 'Human'), ('Half-Human', 'Half-Human'), ('Dwarf', 'Dwarf'), ('Halfling', 'Halfling'), ('Orc', 'Orc'), ('Gnome', 'Gnome'), ('Elf', 'Elf'), ('Half-Elf', 'Half-Elf'), ('Tiefling', 'Tiefling')], default='Human', max_length=50),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.CharField(choices=[('Athletics', 'Athletics'), ('Acrobatics', 'Acrobatics'), ('Sleight of Hand', 'Sleight of Hand'), ('Stealth', 'Stealth'), ('Arcana', 'Arcana'), ('History', 'History'), ('Investigation', 'Investigation'), ('Nature', 'Nature'), ('Religion', 'Religion'), ('Animal Handling', 'Animal Handling'), ('Insight', 'Insight'), ('Medicine', 'Medicine'), ('Perception', 'Perception'), ('Survival', 'Survival'), ('Deception', 'Deception'), ('Intimidation', 'Intimidation'), ('Performance', 'Performance'), ('Persuasion', 'Persuasion')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='strength_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom_bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
