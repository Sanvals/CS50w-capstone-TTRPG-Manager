from django.db.models import F, Case, Value, When, CharField
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .data import skills, skills_stats, equipment_packs, classRecommendation, stats, classSave, class_equipment, classHitDice
from .forms import CharacterForm
from .models import Character, User, Item, Spell, Feat, CharacterItem
from .login import login_view, logout_view, register
import random
import json


# Create your views here.
def index(request):
    # Get the list of the last 10 characters
    characters = Character.objects.order_by('-id')
    
    return render(request, "index.html", {
        "characters": characters,
    })

# Create a stats generator using the 4d6 system
def stats_generator():
    stats = []

    for i in range(6):
        score = 0
        stat = []
        for i in range(4):
            roll = random.randint(1,6)
            stat.append(roll)
        
        stat.sort(reverse=True)
        stat = stat[:3]
        for i in stat:
            score += i
        
        stats.append(score)
    
    stats.sort(reverse=True)
    return stats


# Create a view for the character creator
@login_required(login_url="sheet:login")
def create_character(request):
    # On POST, save the new character
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():        
            # Catch the main info from the form
            name = form.cleaned_data.get("name")
            player = request.user
            race = form.cleaned_data.get("race_choice")          
            character_class = form.cleaned_data.get("class_choice")
            level = form.cleaned_data.get("level")
            skills_chosen = [skill for skill in skills.keys() if request.POST.get(skill)]
            image = form.cleaned_data.get("image")
            hp = form.cleaned_data.get("hp")
            alignment = form.cleaned_data.get("alignment")
            background = form.cleaned_data.get("background")
            gold = request.POST.get("coin_gold")
            # print(f"Name: {name} ({player})\nRace: {race}\nClass: {character_class} lv {level}\nSkills: {', '.join(map(str, skills_chosen))}")
            
            
            # Catch the temporary inventory
            temp_inventory = [] 
            
            iterator = 1
            while (True):
                package = request.POST.get("choice_" + str(iterator))
                if package:
                    temp_inventory.append(package)
                    iterator += 1
                else:
                    break
            
            # Catch the stats
            strength = int(request.POST.get("strength"))
            dexterity = int(request.POST.get("dexterity"))
            constitution = int(request.POST.get("constitution"))
            intelligence = int(request.POST.get("intelligence"))
            wisdom = int(request.POST.get("wisdom"))
            charisma = int(request.POST.get("charisma"))
            ##print(f"STR: {strength}, INT: {intelligence}, DEX: {dexterity}, WIS: {wisdom}, CON: {constitution}, CHA: {charisma}")
            
            # Save the data to the model
            newCharacter = Character(
                # Main info
                name = name,
                player = player,
                level = level,
                character_class = character_class,
                race = race,
                skills = skills_chosen,
                image = image,
                hp = hp,
                alignment = alignment,
                background = background,
                temp_inventory = json.dumps(temp_inventory),
                coin_gold = gold,
                
                # Stats info
                strength = strength,
                dexterity = dexterity,
                constitution = constitution,
                intelligence = intelligence,
                wisdom = wisdom,
                charisma = charisma,
            )
            
            # Save the model and return to index
            newCharacter.save()
            return redirect('index')
        
    # On GET, display the forms
    else:
        # Set the stats in normal, descending order
        statsgen = stats_generator()
        initial_data = {
            'strength': statsgen[0],
            'dexterity': statsgen[1],
            'constitution': statsgen[2],
            'intelligence': statsgen[3],
            'wisdom': statsgen[4],
            'charisma': statsgen[5],
        }
        
        # Display the form
        form = CharacterForm(initial = initial_data)
        
    return render(request, 'create_character.html', {
        'form': form,
        'skills': skills,
        'equipment_packs': equipment_packs,
        'stats': stats,
        
        # Parse the JSON data
        'initial_data_json': json.dumps(initial_data),
        'class_save_json': json.dumps(classSave),
        'class_recommendation_json': json.dumps(classRecommendation),
        'class_equipment_json': json.dumps(class_equipment),
        'class_hitdice_json': json.dumps(classHitDice)
        })


# Page for character viewing
@login_required
def character_page(request, pk):
    character = get_object_or_404(Character, pk=pk)    
    
    # Gather all the data of items and spells from database
    itemsJSON = Item.objects.order_by('id')
    DBitems = serializers.serialize('json', itemsJSON)
    spellsJSON = Spell.objects.order_by('id')
    DBspells = serializers.serialize('json', spellsJSON)
    
    inventoryList = CharacterItem.objects.filter(character=character)

    level_expression = Case (
        When(level="Cantrip", then=Value(0)),
        default=F("level"),
        output_field=CharField()
        )
    
    spells = character.spells.annotate(
        numerical_level=level_expression).order_by('numerical_level')
    
    if not spells:
        spells= None
    
    return render(request, 'character.html', {
        'character': character,
        'class_save_json': json.dumps(classSave),
        'skills_stats': skills_stats,
        'spells': spells,
        'inventory': inventoryList,
        'DBspells': DBspells,
        'DBitems': DBitems,
    })

@csrf_exempt
@login_required
def update_character(request, pk):
    character = get_object_or_404(Character, pk=pk)    

    # Check if the call is a POST method
    if request.method == "POST":
        # Catch the form and the value that is being edited
        form = request.POST.get("form")
        value = request.POST.get("value")

        print(f"Form: {form}, Value: {value}")
        match form:
            case "alignment": character.alignment = value
            case "background": character.background = value
            case "traits": character.traits = value
            case "ideals": character.ideals = value
            case "bonds": character.bonds = value
            case "flaws": character.flaws = value
            case "inspiration": character.inspiration = not character.inspiration
            case "level": character.level = value
            case "newMaxHP": character.hp = value
            case "currentHP": character.currenthp = value
            case "gold-coins": character.coin_gold = value
            case "silver-coins": character.coin_silver = value
            case "copper-coins": character.coin_copper = value
            case "del_temporary": character.temp_inventory = None
            
            case "add_item":
                item_id = int(value)
                item = get_object_or_404(Item, id=item_id)
            
                new_inventory = CharacterItem(character=character, item=item)
                new_inventory.save()
                
            case "delete_item":
                inventory_id = int(value)
                item = get_object_or_404(CharacterItem, id=inventory_id)
                
                item.delete()
            
            case "add_spell":
                spell_id = int(value)
                spell = get_object_or_404(Spell, id=spell_id)
                
                character.spells.add(spell)
                
            case "delete_spell":
                spell_id = int(value)
                spell = get_object_or_404(Spell, id=spell_id)
                
                character.spells.remove(spell)

        character.save()
        
    return render(request, 'character.html', {
        'character': character,
        'class_save_json': json.dumps(classSave),
    })


def databases(request):
    itemsJSON = Item.objects.order_by('id')
    spellsJSON = Spell.objects.order_by('id')
    
    items = serializers.serialize('json', itemsJSON)
    spells = serializers.serialize('json', spellsJSON)
    
    return render(request, 'databases.html', {
        'items': items,
        'spells': spells,
    })
    