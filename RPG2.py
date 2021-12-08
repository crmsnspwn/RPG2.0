from random import randint

## Initialize

game_running = True
game_results = []

## Classes
class armor:
    type = 'Gear'

    def __init__(self, name, allowed_classes, body_part, ac_bonus):
        self.name = name
        self.allowed_class = allowed_classes
        self.body_part = body_part
        self.ac_bonus = ac_bonus

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

class classes:
    type = 'Trait'
    
    def __init__(self, name, stat, hp, ac_bonus) -> None:
        self.name = name
        self.stat1 = stat
        self.hp = hp
        self.ac_bonus = ac_bonus

class races:
    type = 'Trait'

    def __init__(self, name, stat, bonus) -> None:
        self.name = name
        self.stat = stat
        self.bonus = bonus

## Gear
# Armor
leather = armor('Leather',['Bard', 'Cleric', 'Druid', 'Fighter', 'Rogue', 'Sorcerer', 'Wizard'], 'all', 2)
padded = armor('Padded',['Bard', 'Cleric', 'Druid', 'Fighter', 'Rogue', 'Sorcerer', 'Wizard'], 'all', 3)
chain_mail = armor('Chainmail',['Cleric', 'Fighter', 'Paladin'], 'all', 4)
plate_mail = armor('Platemail',['Fighter', 'Paladin'], 'all', 4)

# Weapons



## Traits
# Classes

barbarian = classes('Barbarian', 'Str', 12, 'Con')
bard = classes('Bard', 'Cha', 8, 'None')
cleric = classes('Cleric', 'WIS', 8, 'None')
druid = classes('Druid', 'Wis', 8, 'None')
fighter = classes('Fighter', 'Str', 10, 'None')
monk = classes('Monk', 'Wis', 8, 'Wis')
paladin = classes('Paladin', 'Cha', 10, 'None')
rogue = classes('Rogue', 'Dex', 8, 'None')
sorcerer = classes('Sorcerer', 'Cha', 8, 'None')
wizard = classes('Wizard', 'Int', 8, 'None')

# Races

drow = races('Drow', ['Dex', 'Cha'], [2, 1])
dwarf = races('Dwarf', ['Con', 'Wis'], [2, 1])
elf = races('Drow', ['Dex', 'Wis'], [2, 1])
half_orc = races('Drow', ['Str', 'Con'], [2, 1])
human = races('Drow', ['Str',], [1, 1])