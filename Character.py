# Revision of Character.py
# Testing out different data management tools i.e. nested dictionaries and lists.

import os
import random
def Roll(sides):
    result = random.randint(1,sides)
    return result






class Character:
    
    # attributeModifier = racialBonus + ?
    
    # Creates a character to be used by a player, or used as a non player character.
    def __init__(self,
                 name,
                 race,
                 characterClass) -> None:

        # === Provide basic character information ===
        # Create a name for this Character
        self.name = name
        # Define The Character's Race
        self.race = race
        # Define Character Class
        self.characterClass = characterClass
        # Sets the Starting HP values for the characters based on class, race, and rolls
        # self.maxHP = self.characterClass.base_hp
        # self.currentHP = self.maxHP
        # self.tempHP = 0

        # self.alignment
        # self.background

        # self.size
        # self.height
        # self.weight



        # === Additional Character Information ===
        self.armor_class = 10 # + (armorValue)
        # self.initiative
        # self.speed
        # self.inventory = []
        # self.skills = []
        # self.spells = []
        



        # == Racial Attribute Bonuses ==
        # Adjusts stats based on racial bonuses
        # strengthBonus = race.strength_modifier
        # dexterityBonus = race.dexterity_modifier
        # constitutionBonus = Races.dwarf.constitution_modifier
        # wisdomBonus = race.wisdom_modifier
        # intelligenceBonus = race.intelligence_modifier
        # charismaBonus = race.charisma_modifier



        # When creating a character, create a random base stat block first. May have to move stats around in character creation order to ensure that modifiers get applied correctly
        self.baseStats = {
            'Strength':(Roll(6)*3),
            'Dexterity':(Roll(6)*3),
            'Constitution':(Roll(6)*3),# + constitutionBonus,
            'Wisdom':(Roll(6)*3),
            'Intelligence':(Roll(6)*3),
            'Charisma':(Roll(6)*3)
        }





# Get quick information about a character
def statBlock(target):
    os.system('cls')
    print(f"""Character Name: {target.name}
Character Race: {target.race}
Character Class: {target.characterClass}

============================================================================

Stat Block:

Str: {target.baseStats['Strength']}
Dex: {target.baseStats['Dexterity']}
Con: {target.baseStats['Constitution']}
Wis: {target.baseStats['Wisdom']}
Int: {target.baseStats['Intelligence']}
Cha: {target.baseStats['Charisma']}
          """)














person = Character('Michael','Human','Barbarian')
statBlock(person)