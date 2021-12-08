from random import randint
from tkinter import *


## Classes
# Gear
class armor:
    type = 'Gear'

    def __init__(self, name, allowed_classes, body_part, ac_bonus):
        self.name = name
        self.allowed_class = allowed_classes
        self.body_part = body_part
        self.ac_bonus = ac_bonus

class bag:
    type = 'Gear'

    def __init__(self, name, size, capacity):
        self.name = name
        self.size = size
        self.capacity = capacity

class potions:
    type = "Gear"

    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp

class shield:
    type = 'Gear'

    def __init__(self, name, allowed_classes, ac_bonus):
        self.name = name
        self.allowed_class = allowed_classes
        self.ac_bonus = ac_bonus

class weapon:
    type = 'Gear'

    def __init__(self, name, allowed_classes, hands, modifier, damage):
        self.name = name
        self.allowed_class = allowed_classes
        self.hands = hands
        self.modifier = modifier
        self.damage = damage

# Traits
# Character Classes
class casting_classes:
    type = 'Trait'
    
    def __init__(self, name, stat, hp, spell_slots):
        self.name = name
        self.stat1 = stat
        self.hp = hp
        self.spell_slots = spell_slots

class hybrid_classes:
    type = 'Trait'
    
    def __init__(self, name, stat, hp, ac_bonus, spell_slots, special):
        self.name = name
        self.stat1 = stat
        self.hp = hp
        self.ac_bonus = ac_bonus
        self.spell_slots = spell_slots
        self.special = special

class melee_classes:
    type = 'Trait'
    
    def __init__(self, name, stat, hp, ac_bonus, special):
        self.name = name
        self.stat1 = stat
        self.hp = hp
        self.ac_bonus = ac_bonus
        self.special = special

# Races
class races:
    type = 'Trait'

    def __init__(self, name, stat, bonus):
        self.name = name
        self.stat = stat
        self.bonus = bonus

# Spells
class attack_spells:
    type = 'Spell'

    def __init__(self, name, allowed_classes, modifier, level, damage):
        self.name = name
        self.allowed_classes = allowed_classes
        self.modifier = modifier
        self.level = level
        self.damage = damage

class control_spells:
    type = 'Spell'

    def __init__(self, name, allowed_classes, modifier, level, affect):
        self.name = name
        self.allowed_classes = allowed_classes
        self.modifier = modifier
        self.level = level
        self.affect = affect

## Gear
# Armor

leather = armor('Leather',['Bard', 'Cleric', 'Druid', 'Fighter', 'Rogue', 'Sorcerer', 'Wizard'], 'all', 2)
padded = armor('Padded',['Bard', 'Cleric', 'Druid', 'Fighter', 'Rogue', 'Sorcerer', 'Wizard'], 'all', 3)
chain_mail = armor('Chainmail',['Cleric', 'Fighter', 'Paladin'], 'all', 4)
plate_mail = armor('Platemail',['Fighter', 'Paladin'], 'all', 4)

# Bags

small_bag = bag('Small Bag', 'small', 5)
medium_bag = bag('Medium Bag', 'medium', 10)
large_bag = bag('Large Bag', 'large', 15)

# Potions

small_healling = potions('Healing Draught', 'health', 4)
large_healing = potions('Healing Bottle', 'health', 8)
small_poison = potions('Poison Draught', 'damage', 4)
large_poison = potions('Poison Bottle', 'damage', 8)

# Shields

buckler = shield('Buckler', ['barbarian', 'druid', 'fighter'], 2)
round_shield = shield('Round Shield', ['barbarian', 'fighter', 'paladin'], 3)
tower_shield = shield('Tower Shield', ['fighter', 'paladin'], 4)

# Weapons

club = weapon('Club', ['barbarian', 'druid', 'fighter'], 1, 'Str', 4)
dagger = weapon('Dagger', ['bard', 'fighter', 'rogue'], 1, 'Dex', 4)
great_axe = weapon('Great Axe', ['barbarian', 'fighter'], 2, 'Str', 12)
great_club = weapon('Greatclub', ['barbarian', 'fighter'], 2, 'Str', 8)
great_sword = weapon('Great Axe', ['fighter', 'paladin'], 2, 'Str', 12)
long_sword = weapon('Long Sword', ['barbarian', 'fighter', 'paladin', 'rogue'], 1, 'Str', 8)
rapier = weapon('Rapier',['bard', 'fighter', 'paladin', 'rogue'], 1, 'Dex', 8)
spell_book = weapon('Spell Book', ['Sorcerer'], 1, 'Cha', 0)
unarmed = weapon('Unarmed', ['monk'], 2, 'Dex', 8)
wand = weapon('Wand',['Wizard'], 1, 'Int', 0)

## Traits
# Melee Classes

barbarian = melee_classes('Barbarian', 'Str', 12, 'Con', 'rage')
fighter = melee_classes('Fighter', 'Str', 10, 'None', 'action_surge')
monk = melee_classes('Monk', 'Wis', 8, 'Wis', 'flurry_of_blows')
rogue = melee_classes('Rogue', 'Dex', 8, 'None', 'sneak_attack')

# Casting Classes

bard = casting_classes('Bard', 'Cha', 8, 10)
sorcerer = casting_classes('Sorcerer', 'Cha', 8, 10)
wizard = casting_classes('Wizard', 'Int', 8, 10)

# Hybrid Classes

cleric = hybrid_classes('Cleric', 'WIS', 8, 'None', 6, 'turn_undead')
druid = hybrid_classes('Druid', 'Wis', 8, 'None', 6, 'wild_shape')
paladin = hybrid_classes('Paladin', 'Cha', 10, 'None', 6, 'smite')

# Races

drow = races('Drow', ['Dex', 'Cha'], [2, 1])
dwarf = races('Dwarf', ['Con', 'Wis'], [2, 1])
elf = races('Drow', ['Dex', 'Wis'], [2, 1])
half_orc = races('Drow', ['Str', 'Con'], [2, 1])
human = races('Drow', ['Str', 'Int'], [1, 1])

# Special



# Spells

fire_bolt = attack_spells('Fire Bolt', ['Wizard'], 'Int', 1, 8)
lightning_bolt = attack_spells('Lightning Bolt', ['Wizard'], 'Int', 3, 30)

##########################################################################
## Initialize

game_running = True
game_results = []
