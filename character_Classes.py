# This page will store all of the available playable character classes.
import random
class Character_Class:

    # This defines the blueprint for a playable character class in the world of DnD

    def __init__(self,name,hit_die,description) -> None:

        # ===== Basic Information =============================================
        # Define the name of the character class.
        self.name = name

        # Define the hit die used by the class. This is used to determine starting health and how much health gained when levling up.
        self.hit_die = hit_die

        # This is the HP that the class starts with whenever it is created at level 1. 
        self.base_hp = hit_die
        self.description = description

        # ===== Character Class Skills =============================================
        # Define the skills available to the class
        self.skills = []

        # ===== Saving Throw Proficiencies =============================================



        # ===== Primary Ability =============================================




        # ===== Armor and Weapon Proficiencies =============================================
        






# ========== Creating the 12 standard classes from the Players Handbook ====================================


barbarian = Character_Class(
    name='Barbarian',
    hit_die=12,
    description='A fierce warrior who can enter a battle rage'   
)

bard = Character_Class(
    name='Bard',
    hit_die=8,
    description='An inspiring magician whose power echoes the music of creation.'
)

cleric = Character_Class(
    name='Cleric',
    hit_die=8,
    description='A priestly champion who wields divine magic in service of a higher power.'
)

druid = Character_Class(
    name='Druid',
    hit_die=8,
    description='A priest of the Old Faith, wielding the powers of nature -- moonlight and plant growth, fire and lightning -- and adopting animal forms.'
)

fighter = Character_Class(
    name='Fighter',
    hit_die=10,
    description='A master of martial combat, skilled with a variety of weapons and armor.'
)

monk = Character_Class(
    name='Monk',
    hit_die=8,
    description='A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.'
)

paladin = Character_Class(
    name='Paladin',
    hit_die=10,
    description='A holy warrior bound to a sacred oath.'
)

ranger = Character_Class(
    name='Ranger',
    hit_die=8,
    description='A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.'
)

rogue = Character_Class(
    name='Rogue',
    hit_die=6,
    description='A scoundrel who uses stealth and ckery to overcome obstacles and enemies.'
)

sorcerer = Character_Class(
    name='Sorcerer',
    hit_die=6,
    description='A spellcaster who draws on inherent magic from a gift or bloodline.'
)

warlock = Character_Class(
    name='Warlock',
    hit_die=8,
    description='A wielder of magic that is derived from a bargain with an extraplanar entity.'
)

wizard = Character_Class(
    name='Wizard',
    hit_die=6,
    description='A scholarly magic-user capable of manipulating the structures of reality.'
)