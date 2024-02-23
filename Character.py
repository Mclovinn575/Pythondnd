# Made by Michael Love III
import os
import random
import Races


def Roll(sides):
    result = random.randint(1,sides)
    return result



# Create Player Character
class Character:


        def __init__(self, name, race) -> None:

        # Establish base character attributes
                self.strength=(Roll(6)*2) +6
                self.dexterity=(Roll(6)*2) +6
                self.constitution=(Roll(6)*2) +6
                self.wisdom=(Roll(6)*2) +6
                self.intelligence=(Roll(6)*2) +6
                self.charisma=(Roll(6)*2) +6
        # Verified that these stats do work and are manipulated based on the race you choose.

        # Establish basic character qualities
                self.name = name
                self.race = Races.Dwarf
                # self.alignment = input("Alignment: ")
                # self.background = input("Background: ")
                # self.char_class = input("Character Class: ")
                self.level = 0
                # self.faction = ""
                # self.height = ""
                # self.weight = input("Character Weight: ")

                # This does work, however I need to test that it will overwrite correctly
                self.strength = self.strength + race.strength_modifier
                self.dexterity = self.dexterity + race.dexterity_modifier
                self.constitution = self.constitution + race.constitution_modifier
                self.wisdom = self.wisdom + race.wisdom_multiplier
                self.intelligence = self.intelligence + race.intelligence_modifier
                self.charisma = self.charisma + race.charisma_modifier

        # Extra character details

                self.armor_class = 10
                self.initiative = 0
                self.speed = (self.race)
                self.max_hp = 100
                self.current_hp = self.max_hp
                self.skills = []
                self.temp_hp = 0
                self.spells = []
                self.equipment = []

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




def stat_block():
        print(f"""
Character Name: {hero.name}

=== Character Stats ===
Str: {hero.strength}
Dex: {hero.dexterity}
Con: {hero.constitution}
Wis: {hero.wisdom}
Int: {hero.intelligence}
Cha: {hero.charisma}

=== Character Information ===
        == Racial Abilities ==
{hero.race.racial_abilities}

        == Languages ==
{hero.race.language}
      """)







# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


os.system('cls')

hero = Character("Dwargo", Races.Dwarf)
stat_block()










































# spells = {
#     'Darkvision':'Ability to see up to 30 feet in the dark'
#     ,'Dwarven Resilience' : 'Grants additional poison resistance'
# }
# # Iterates through each spell and it's description.
# for spell in spells.items():
#     print(f'{spell[0]} : {spell[1]}')
    


