classRecommendation = {
    'Barbarian': ['strength', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'charisma'],
    'Bard': ['charisma', 'dexterity', 'constitution', 'wisdom', 'intelligence', 'strength'],
    'Cleric': ['wisdom', 'constitution', 'strength', 'intelligence', 'dexterity', 'charisma'],
    'Druid': ['wisdom', 'constitution', 'dexterity', 'intelligence', 'strength', 'charisma'],
    'Fighter': ['strength', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'charisma'],
    'Monk': ['dexterity', 'wisdom', 'constitution', 'intelligence', 'strength', 'charisma'],
    'Paladin': ['strength', 'constitution', 'charisma', 'wisdom', 'intelligence', 'dexterity'],
    'Ranger': ['dexterity', 'wisdom', 'constitution', 'intelligence', 'strength', 'charisma'],
    'Rogue': ['dexterity', 'intelligence', 'constitution', 'wisdom', 'strength', 'charisma'],
    'Sorcerer': ['charisma', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'strength'],
    'Warlock': ['charisma', 'constitution', 'dexterity', 'wisdom', 'intelligence', 'strength'],
    'Wizard': ['intelligence', 'constitution', 'dexterity', 'wisdom', 'strength', 'charisma'],
}

classSave = {
    "Barbarian": ["strength", "constitution"],
    "Bard": ["dexterity", "charisma"],
    "Cleric": ["wisdom", "charisma"],
    "Druid": ["intelligence", "wisdom"],
    "Fighter": ["strength", "constitution"],
    "Monk": ["strength", "dexterity"],
    "Paladin": ["wisdom", "charisma"],
    "Ranger": ["strength", "dexterity"],
    "Rogue": ["dexterity", "intelligence"],
    "Sorcerer": ["constitution", "charisma"],
    "Warlock": ["wisdom", "charisma"],
    "Wizard": ["intelligence", "wisdom"]
}

classHitDice = {
    "Barbarian": 12,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Fighter": 10,
    "Monk": 8,
    "Paladin": 10,
    "Ranger": 10,
    "Rogue": 8,
    "Sorcerer": 6,
    "Warlock": 8,
    "Wizard": 6,
}

skills = {
    "Acrobatics": "Vaulting over a barrel of tomatoes.",
    "Animal Handling": "Trying to convince a nearby fox to eat a tomato.",
    "Arcana": "Recognising that you have seen the symbol on a tomato barrel is a magic rune.",
    "Athletics": "Lifting a heavy barrel of tomatoes.",
    "Deception": "Telling the druid you never gave the fox a tomato.",
    "History": "Remembering that you have seen a similar symbol on another barrel of romatoes.",
    "Insight": "Recognising that the fox doesn't like tomatoes by body language.",
    "Intimidation": "Threatening the fox to eat more tomatoes.",
    "Investigation": "Checking if there are more symbols on other tomato barrels.",
    "Medicine": "Putting the fox in recovery position after eating a bad tomato.",
    "Nature": "Knowing that if the tomato was in the sun for too long, it would be wrinkyl now.",
    "Perception": "Spotting a druid watching you behind a tree.",
    "Performance": "Performing a dance so godo the fox forgives you.",
    "Persuasion": "Convincing the druid to let you go if you go a good dance for him.",
    "Religion": "Knowing that the Goddess of nature bequeaths gifs to her bests tomato farmers.",
    "Sleight of Hand": "Discretely putting a tomato in your pocket.",
    "Stealth": "Sneaking behind the person selling tomatoes.",
    "Survival": "Follow tracks of a fox.",
}

skills_stats = {
    "Acrobatics": "dexterity",
    "Animal Handling": "wisdom",
    "Arcana": "intelligence",
    "Athletics": "strength",
    "Deception": "charisma",
    "History": "intelligence",
    "Insight": "wisdom",
    "Intimidation": "charisma",
    "Investigation": "intelligence",
    "Medicine": "wisdom",
    "Nature": "intelligence",
    "Perception": "wisdom",
    "Performance": "charisma",
    "Persuasion": "charisma",
    "Religion": "intelligence",
    "Sleight of Hand": "dexterity",
    "Stealth": "dexterity",
    "Survival": "wisdom",
}

stats = {
    "Strength": "How easily you can crush a tomato.",
    "Dexterity": "How easily you can catch a tomato.",
    "Constitution": "How easily you could eat a rotten tomato without getting sick.",
    "Intelligence": "Helps you know that a tomato is a fruit, not a vegetable.",
    "Wisdom": "Help you know that just because a tomato is a fruit, does not mean it belongs to a salad.",
    "Charisma": "Helps you convince people to eat a tomato-filled fruit salad.",
}

equipment_packs = {
    "Explorers Pack": [
        "Backpack",
        "Bedroll",
        "Mess Kit",
        "Tinderbox",
        "10 Torches",
        "10 Days of Rations",
        "Waterskin",
        "50 feet of Hempen Rope",
    ],
    "Dungeoneers Pack": [
        "Backpack",
        "Crowbar",
        "Hammer",
        "10 Pitons",
        "10 Torches",
        "10 Days of Rations",
        "Waterskin",
        "50 feet of Hempen Rope",
    ],
    "Burglars Pack": [
        "Backpack",
        "Bag of 1000 Ball Bearings",
        "10 Feet of String",
        "Bell",
        "Candle (5)",
        "Crowbar",
        "Hammer",
        "10 Pitons",
        "Hooded Lantern",
        "2 Flasks of Oil",
        "5 Days of Rations",
        "Tinderbox",
        "Waterskin",
        "50 feet of Hempen Rope",
    ],
    "Scholars Pack": [
        "Backpack",
        "Book of Lore",
        "Ink (1 ounce bottle)",
        "Ink Pen",
        "10 Sheets of Parchment",
        "Little Bag of Sand",
        "Small Knife",
    ]
}

class_equipment = {
    "Barbarian": {
        "choice_1": ["a greataxe", "any martial melee weapon"],
        "choice_2": ["two handaxes", "any simple weapon"],
        "choice_3": ["An explorer's pack and four javelins"]
    },
    
    "Bard": {
        "choice_1": ["a rapier", "a longsword", "any simple weapon"],
        "choice_2": ["a diplomat's pack", "entertainer's pack"],
        "choice_3": ["a lute", "any other musical instrument"],
        "choice_4": ["leather armor and a dagger"]
    },
    
    "Cleric": {
        "choice_1": ["a mace", "a warhammer"],
        "choice_2": ["scale mail", "leather armor", "chain mail"],
        "choice_3": ["a light crossbow and 20 bolts", "any simple weapon"],
        "choice_4": ["a priest's pack", "an explorer's pack"],
        "choice_5": ["a shield", "a holy symbol"]
    },
    
    "Druid": {
        "choice_1": ["a wooden shield", "any simple weapon"],
        "choice_2": ["a scimitar", "any simple melee weapon"],
        "choice_3": ["leather armor", "an explorer's pack", "a druidic focus"]
    },
    
    "Fighter": {
        "choice_1": ["chain mail", "leather armor, longbow, 20 arrows"],
        "choice_2": ["a martial weapon and a shield", "two martial wepons"],
        "choice_3": ["a light crossbow and 20 bolts", "two handaxes"],
        "choice_4": ["a sungeoneer's pack", "an explorer's pack"]
    },
    
    "Monk": {
        "choice_1": ["a shortsword", "any simple weapon"],
        "choice_2": ["a dungeoneer's pack", "an explorer's pack"],
        "choice_3": ["10 darts"]
    },

    "Paladin": {
        "choice_1": ["a martial weapon and a shield", "two martial weapons"],
        "choice_2": ["five javelins", "any simple melee weapon"],
        "choice_3": ["a priest's pack", "an explorer's pack"],
        "choice_4": ["Chain mail and a holy symbol"]
    },

    "Ranger": {
        "choice_1": ["scale mail", "leather armor"],
        "choice_2": ["two shortswords", "two simple melee weapons"],
        "choice_3": ["a dungeoneer's pack", "an explorer's pack"],
        "choice_4": ["A longbow and a quiver of 20 arrows"]
    },
    
    "Rogue": {
        "choice_1": ["a rapier", "a shortsword"],
        "choice_2": ["a shortbow and quiver of 20 arrows", "a shortsword"],
        "choice_3": ["a burglar's pack", "a dungeoneer's pack", "an explorer's pack"],
        "choice_4": ["leather armor, two daggers and thieves' tools"]
    },
    
    "Sorcerer": {
        "choice_1": ["a light crossbow and 20 bolts", "any simple weapon"],
        "choice_2": ["a component pouch", "an arcane focus"],
        "choice_3": ["a dungeoneer's pack", "an explorer's pack"],
        "choice_4": ["two daggers"]
    },
    
    "Warlock": {
        "choice_1": ["a light crossbow and 20 bolts", "any simple weapon"],
        "choice_2": ["a component pouch", "an arcane focus"],
        "choice_3": ["a scholar's pack", "a dungeoneer's pack"],
        "choice_4": ["leather armor, any simple weapon and two daggers"]
    },

    "Wizard": {
        "choice_1": ["a quarterstaff", "a dagger"],
        "choice_2": ["a component pouch", "an arcane focus"],
        "choice_3": ["a scholar's pack", "an explorer's pack"],
        "choice_4": ["a spellbook"]
    },
}