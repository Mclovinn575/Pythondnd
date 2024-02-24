# Made by Michael Love III
import os
import random
import Races
import character_Classes


def Roll(sides):
    result = random.randint(1,sides)
    return result



# Create Player Character
class Character:


        def __init__(self, name, race) -> None:

        # Establish base character attributes
        # Rolls with 2d6 +6
        # Feels a bit more beginner friendly (stat heavy)
                # self.strength=(Roll(6)*2) +6
                # self.dexterity=(Roll(6)*2) +6
                # self.constitution=(Roll(6)*2) +6
                # self.wisdom=(Roll(6)*2) +6
                # self.intelligence=(Roll(6)*2) +6
                # self.charisma=(Roll(6)*2) +6
        # Rolls with 3d6 
        # Feels a little more natural
                self.strength=(Roll(6)*3) 
                self.dexterity=(Roll(6)*3)
                self.constitution=(Roll(6)*3)
                self.wisdom=(Roll(6)*3) 
                self.intelligence=(Roll(6)*3)
                self.charisma=(Roll(6)*3) 
        # Verified that these stats do work and are manipulated based on the race you choose.

        # Establish basic character qualities
                self.name = name
                self.race = race
                # self.alignment = input("Alignment: ")
                # self.background = input("Background: ")
                self.char_class = character_Classes.barbarian
                self.level = 0
                # self.faction = ""
                # self.height = ""
                # self.weight = input("Character Weight: ")

                # This does work, however I need to test that it will overwrite correctly
                self.strength = self.strength + race.strength_modifier
                self.dexterity = self.dexterity + race.dexterity_modifier
                self.constitution = self.constitution + race.constitution_modifier
                self.wisdom = self.wisdom + race.wisdom_modifier
                self.intelligence = self.intelligence + race.intelligence_modifier
                self.charisma = self.charisma + race.charisma_modifier

        # Extra character details

                self.armor_class = 10
                self.initiative = 0
                self.speed = (self.race)
                # need to make sure to add the attribute bonuses based on how high the number is. ex) str: 15 = +3
                self.max_hp = self.char_class.base_hp 
                self.current_hp = self.max_hp
                self.skills = []
                self.temp_hp = 0
                self.spells = []
                self.equipment = []

        

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




def stat_block(target):
        print(f"""
Character Name: {target.name}
Race: {target.race.name}
Character Class: {target.char_class.name}

Max HP: {target.max_hp}
Current HP: {target.current_hp}

=== Character Stats ===
Str: {target.strength}
Dex: {target.dexterity}
Con: {target.constitution}
Wis: {target.wisdom}
Int: {target.intelligence}
Cha: {target.charisma}

=== Character Information ===

        == Racial Abilities ==
{target.race.racial_abilities}

        == Languages ==
{target.race.language}
      """)







# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


os.system('cls')

dwarf = Character("Dwargo", Races.dwarf)
stat_block(dwarf)
print(dwarf.char_class.name)

# elf = Character("Livia", Races.elf)
# stat_block(elf)

# human = Character("Michael", Races.human)
# stat_block(human)



















# spells = {
#     'Darkvision':'Ability to see up to 30 feet in the dark'
#     ,'Dwarven Resilience' : 'Grants additional poison resistance'
# }
# # Iterates through each spell and it's description.
# for spell in spells.items():
#     print(f'{spell[0]} : {spell[1]}')
    


