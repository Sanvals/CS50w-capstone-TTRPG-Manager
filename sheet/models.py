from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

class Character(models.Model):
    # Basic information
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_player")
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    image = models.URLField(blank=True)
    hp = models.IntegerField(default=1)
    currenthp = models.IntegerField(default=1)
    alignment = models.CharField(blank=True, max_length=50)
    background = models.CharField(blank=True, max_length=50)
    traits = models.CharField(blank=True, max_length= 50)
    ideals = models.CharField(blank=True, max_length= 50)
    bonds = models.CharField(blank=True, max_length= 50)
    flaws = models.CharField(blank=True, max_length= 50)
    initiative = models.IntegerField(default=10)
    armorclass = models.IntegerField(default=10)
    speed = models.IntegerField(default=30)
    inspiration = models.BooleanField(default=False)
    
    BARBARIAN = 'Barbarian'
    BARD = 'Bard'
    CLERIC = 'Cleric'
    DRUID = 'Druid'
    FIGHTER = 'Fighter'
    MONK = 'Monk'
    PALADIN = 'Paladin'
    RANGER = 'Ranger'
    ROGUE = 'Rogue'
    SORCERER = 'Sorcerer'
    WARLOCK = 'Warlock'
    WIZARD = 'Wizard'
    CLASS_CHOICES = [
        (BARBARIAN, 'Barbarian'),
        (BARD, 'Bard'),
        (CLERIC, 'Cleric'),
        (DRUID, 'Druid'),
        (FIGHTER, 'Fighter'),
        (MONK, 'Monk'),
        (PALADIN, 'Paladin'),
        (RANGER, 'Ranger'),
        (ROGUE, 'Rogue'),
        (SORCERER, 'Sorcerer'),
        (WARLOCK, 'Warlock'),
        (WIZARD, 'Wizard'),
    ]
    character_class = models.CharField(default=BARBARIAN, max_length=20, choices=CLASS_CHOICES)

    HUMAN = "Human"
    HALFHUMAN = "Half-Human"
    DWARF = "Dwarf"
    HALFLING = "Halfling"
    ORC = "Orc"
    GNOME = "Gnome"
    ELF = "Elf"
    HALFELF = "Half-Elf"
    TIEFLING = "Tiefling"
    RACE_CHOICES = [
        (HUMAN, "Human"),
        (HALFHUMAN, "Half-Human"),
        (DWARF, "Dwarf"),
        (HALFLING, "Halfling"),
        (ORC, "Orc"),
        (GNOME, "Gnome"),
        (ELF, "Elf"),
        (HALFELF, "Half-Elf"),
        (TIEFLING, "Tiefling")
    ]
    race = models.CharField(default=HUMAN, max_length=50, choices=RACE_CHOICES)
    
    # Stats
    strength = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dexterity = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    constitution = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    intelligence = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    
    # Stats bonuses
    strength_bonus = models.IntegerField(blank=True, null=True)
    dexterity_bonus = models.IntegerField(blank=True, null=True)
    constitution_bonus = models.IntegerField(blank=True, null=True)
    intelligence_bonus = models.IntegerField(blank=True, null=True)
    wisdom_bonus = models.IntegerField(blank=True, null=True)
    charisma_bonus = models.IntegerField(blank=True, null=True)
    
    # Skills
    ATHLETICS = "Athletics"
    ACROBATICS = "Acrobatics"
    SLEIGHTOFHAND = "Sleight of Hand"
    STEALTH = "Stealth"
    ARCANA = "Arcana"
    HISTORY = "History"
    INVESTIGATION = "Investigation"
    NATURE = "Nature"
    RELIGION = "Religion"
    ANIMALHANDLING = "Animal Handling"
    INSIGHT = "Insight"
    MEDICINE = "Medicine"
    PERCEPTION = "Perception"
    SURVIVAL = "Survival"
    DECEPTION = "Deception"
    INTIMIDATION = "Intimidation"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    SKILLS_CHOICES = [
        (ATHLETICS, "Athletics"),
        (ACROBATICS, "Acrobatics"),
        (SLEIGHTOFHAND, "Sleight of Hand"),
        (STEALTH, "Stealth"),
        (ARCANA, "Arcana"),
        (HISTORY, "History"),
        (INVESTIGATION, "Investigation"),
        (NATURE, "Nature"),
        (RELIGION, "Religion"),
        (ANIMALHANDLING, "Animal Handling"),
        (INSIGHT, "Insight"),
        (MEDICINE, "Medicine"),
        (PERCEPTION, "Perception"),
        (SURVIVAL, "Survival"),
        (DECEPTION, "Deception"),
        (INTIMIDATION, "Intimidation"),
        (PERFORMANCE, "Performance"),
        (PERSUASION, "Persuasion")
    ]
    # USE A JSON OR A LIST FIELD INSTEAD
    skills = models.CharField(max_length=500, null=True, blank=True)
    
    # Inventory
    inventorylist = models.ManyToManyField("Item", through="CharacterItem", blank=True, related_name="users_inventorylist")

    # USE A LIST FIELD INSTEAD
    temp_inventory = models.CharField(max_length=100, blank=True, null=True, default="None")
    
    # Spells
    spells = models.ManyToManyField("Spell", blank=True, related_name="users_spells")
    
    # Coins
    coin_gold = models.PositiveIntegerField(default=0, blank=False)
    coin_silver = models.PositiveIntegerField(default=0, blank=False)
    coin_copper = models.PositiveIntegerField(default=0, blank=False)
    
    def __str__(self):
        return f"{self.player} created a {self.name.title()}"
    
    def save(self, *args, **kwargs):
        self.calculate_stat_bonuses()
        super(Character, self).save(*args, **kwargs)
    
    def calculate_stat_bonuses(self):
        self.strength_bonus = (self.strength - 10) // 2
        self.dexterity_bonus = (self.dexterity - 10) // 2
        self.constitution_bonus = (self.constitution - 10) // 2
        self.intelligence_bonus = (self.intelligence - 10) // 2
        self.wisdom_bonus = (self.wisdom - 10) // 2
        self.charisma_bonus = (self.charisma - 10) // 2
    
    def calculate_other_bonuses(self):
        self.initiative = self.dexterity_bonus
        self.armorclass = self.dexterity_bonus


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    source = models.CharField(max_length=10, blank=False)
    rarity = models.CharField(max_length=50, blank=False, default="None")
    type = models.CharField(max_length=100, blank=False)
    attunement = models.BooleanField(default=False)
    properties = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=9000, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.name.title()}, category: {self.type}"


class CharacterItem(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.character.name.title()} owns {self.quantity} {self.item.name.title()}"


class Spell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    source = models.CharField(max_length=10, blank=False)
    level = models.CharField(max_length=7, blank=False, default="Cantrip")
    casting = models.CharField(max_length=20, blank=False)
    duration = models.CharField(max_length=100, default="Instantaneous")
    school = models.CharField(max_length=50, null=True, blank=True)
    range = models.CharField(max_length=50, null=True, blank=True)
    components = models.CharField(max_length=6, null=True, blank=True)
    cost = models.CharField(max_length=100, null=True, blank=True)
    classes = models.CharField(max_length=100, null=True, blank=True)
    optional = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=9000, null=True, blank=True)
    higher = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id}: {self.name.title()} category: {self.school}"


class Feat(models.Model):
    pass
