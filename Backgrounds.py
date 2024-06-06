# Made by Michael Love III
# 
# This file is meant to store the different background options available to characters. Includes the descriptions, and effect changes for the character.



class Background:


    # Establish Character Background blueprint.
    def __init__(self, description, skill_proficiencies, languages, equipment, features, suggested_characteristics, personality_traits, ideals, bonds, flaws) -> None:
        self.description = description
        self.skill_proficiencies = skill_proficiencies
        self.languages = languages
        self.equipment = equipment
        self.features = features
        self.suggested_characteristics = suggested_characteristics
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Establish character backgrounds

acolyte = Background(
    description="You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices in order to conduct worshippers into the presnces of the divine. You are not necessarily a cleric -- performing sacred rites is not the same thing as channeling divine power.",
    skill_proficiencies=['Inisight','Religion']
    languages="Two of your choosing",
    equipment=['A holy symbol', 'A prayer book', '5 sticks of incense', 'Vestments', 'A set of common clothes', '15 gp'],
    features="As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring comapanions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. THose who share your religion will support you (but only you) at a modest lifestyle.\nYou might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the tempole where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the preists for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.",
    suggested_characteristics='Acolytes are shaped by their experience in temples or other religious communities. Their study of the history and tenets of their faith and their relationships to temples, shrines, or hierarchies affect their mannerisms and ideals. Their flaws might be some hidden hypocrisy or heretical idea, or an ideal or bond taken to an extreme.',
    personality_traits=

)