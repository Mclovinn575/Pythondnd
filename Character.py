# Revision of Character.py
# Testing out different data management tools i.e. nested dictionaries and lists.

import Races
import character_Classes
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

        # ============= Provide basic character information ===========================================================
        # Create a name for this Character
        self.name = name
        # Define The Character's Race
        self.race = race
        # Define Character Class
        self.characterClass = characterClass

        # Sets the Starting HP values for the characters based on class, race, and rolls
        self.maxHP = self.characterClass.base_hp
        self.currentHP = self.maxHP
        self.tempHP = 0

        # self.alignment
        # self.background

        # self.size
        # self.height
        # self.weight



        # ============= Additional Character Information ===============================================================
        self.armor_class = 10 # + (armorValue)
        # self.initiative
        # self.speed
        # self.inventory = []
        # self.skills = []
        # self.spells = []
        



        # ============ Racial Attribute Bonuses ========================================================================
        # Adjusts stats based on racial bonuses
        strengthBonus = race.strength_bonus
        dexterityBonus = race.dexterity_bonus
        constitutionBonus = race.constitution_bonus
        wisdomBonus = race.wisdom_bonus
        intelligenceBonus = race.intelligence_bonus
        charismaBonus = race.charisma_bonus
    




        # When creating a character, create a random base stat block first. May have to move stats around in character creation order to ensure that modifiers get applied correctly
        self.baseStats = {
            'Strength':(Roll(6)*3)+strengthBonus,
            'Dexterity':(Roll(6)*3)+dexterityBonus,
            'Constitution':(Roll(6)*3)+constitutionBonus,
            'Wisdom':(Roll(6)*3)+wisdomBonus,
            'Intelligence':(Roll(6)*3)+intelligenceBonus,
            'Charisma':(Roll(6)*3)+charismaBonus
        }

        # ============ Ability Modifiers ========================================================================
        # self.strengthModifier = 0
        def Strength_Modifier():
            if self.baseStats['Strength'] <= 10 or self.baseStats['Strength'] >=11:
                self.strengthModifier = 0
            elif self.baseStats['Strength'] <= 12 or self.baseStats['Strength'] >=13:
                self.strengthModifier = 1
            elif self.baseStats['Strength'] <= 14 or self.baseStats['Strength'] >=15:
                self.strengthModifier = 2
            elif self.baseStats['Strength'] <= 16 or self.baseStats['Strength'] >=17:
                self.strengthModifier = 3
            elif self.baseStats['Strength'] <= 18 or self.baseStats['Strength'] >=19:
                self.strengthModifier = 4
            elif self.baseStats['Strength'] <= 20 or self.baseStats['Strength'] >=21:
                self.strengthModifier = 5








        # ========== Define Character Actions ==================================================================================
        # Stows item in inventory.
        def Stow():
            pass
        # Equips an item located in the inventory.
        def Equip():
            pass

        # Removes equipped item and places in inventory.
        def Remove():
            pass

        # Drops the item from inventory.
        def Drop():
            pass
        

        # ========== Saving/Loading Data ==================================================================================
        def Save_Character():
            pass

        def Load_Character():
            pass

        def Delete_Character():
            pass







# Get quick information about a character
def statBlock(target):
    os.system('cls')
    print(f"""Character Name: {target.name}
Character Race: {target.race.name}
Character Class: {target.characterClass.name}

HP: {target.currentHP}/{target.maxHP}

============================================================================

Stat Block:

Str: {target.baseStats['Strength']}
Dex: {target.baseStats['Dexterity']}
Con: {target.baseStats['Constitution']}
Wis: {target.baseStats['Wisdom']}
Int: {target.baseStats['Intelligence']}
Cha: {target.baseStats['Charisma']}
          """)













os.system('cls')
person = Character('Michael',Races.dwarf,character_Classes.barbarian)
# statBlock(person)

print(person.baseStats['Strength'])
print(person.strengthModifier)




