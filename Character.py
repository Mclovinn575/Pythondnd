# Revision of Character.py
# Testing out different data management tools i.e. nested dictionaries and lists.

import Armory
import Races
import character_Classes
import os
import random
def Roll(sides):
    result = random.randint(1,sides)
    return result

def Roll20():
    return Roll(20)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Character:

# Attribute modifiers may have to be written in the main app file.
    # could possibly have to hard code it into certain action instead or possibly into the Roll Function
    
    



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
        self.gainedhp = 0
        self.maxHP = self.characterClass.hit_die
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
        self.inventory = []
        
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

       

        


       

        






        # ========== Define Character Actions ==================================================================================
        # Stows item in inventory.
    def Stow(self,item):
        self.inventory.append(item)
    

    # # Equips an item located in the inventory.
    # def Equip():
    #     pass

    # # Removes equipped item and places in inventory.
    # def Remove():
    #     pass

    # # Drops the item from inventory.
    # def Drop():
    #     pass
    

    # # ========== Saving/Loading Data ==================================================================================
    # def Save_Character():
    #     pass

    # def Load_Character():
    #     pass

    # def Delete_Character():
    #     pass
        







    # # ========== Establishing Attribute Modifiers ==================================================================================
    @property
    def strength_modifier(self):
        return ((self.baseStats['Strength'] - 10) //2)
    @property
    def dexterity_modifier(self):
        return ((self.baseStats['Dexterity'] - 10) //2)
    @property
    def constitution_modifier(self):
        return ((self.baseStats['Constitution'] - 10) //2)
    @property
    def wisdom_modifier(self):
        return ((self.baseStats['Wisdom'] - 10) //2)
    @property
    def intelligence_modifier(self):
        return ((self.baseStats['Intelligence'] - 10) //2)
    @property
    def charisma_modifier(self):
        return ((self.baseStats['Charisma'] - 10) //2)



    
    
    



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




# Get quick information about a character
def statBlock(target):
    os.system('cls')
    print(f"""Character Name: {target.name}
Character Race: {target.race.name}
Character Class: {target.characterClass.name}

HP: {target.currentHP}/{target.maxHP}

Inventory: {', '.join(item.name for item in target.inventory)}

============================================================================

Stat Block:

Str: {target.baseStats['Strength']}
Dex: {target.baseStats['Dexterity']}
Con: {target.baseStats['Constitution']}
Wis: {target.baseStats['Wisdom']}
Int: {target.baseStats['Intelligence']}
Cha: {target.baseStats['Charisma']}


Attribute Modifiers:

Str: {target.strength_modifier}
Dex: {target.dexterity_modifier}
Con: {target.constitution_modifier}
Wis: {target.wisdom_modifier}
Int: {target.intelligence_modifier}
Cha: {target.charisma_modifier}

          """)













