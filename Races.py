# A collection of races found throughout the land.input
# Based in Faerun


class Race:
    

    # These are provided whenever a new race is created.
    def __init__(self
                 ,race_name
                 ,adult_age
                 ,lifespan
                 ,size
                 ,speed
                 ,language
                 ,description
                 ,racial_abilities
                 ,strength_modifier
                 ,dexterity_modifier
                 ,constitution_modifier
                 ,wisdom_modifier
                 ,intelligence_modifier
                 ,charisma_modifier
                 ) -> None:

        
        
        
        # Establishes the name and ability modifier of the race
        self.name = race_name
        
        # The age entry determines when a memeber of a race becomes an 'Adult'
        self.adult_age = adult_age
        self.lifespan = lifespan

        # Large Size = 8+ feet tall
        # Medium Size = 4 - 8 feet tall
        # Small Size = 2 - 4 feet tall
            # A characters size can affect different gameplay rules and can cause the character to react differently to certain actions.
        self.size = size

        # Attribute Modifiers
         
        self.strength_modifier = strength_modifier
        self.dexterity_modifier = dexterity_modifier
        self.constitution_modifier = constitution_modifier
        self.wisdom_modifier = wisdom_modifier
        self.intelligence_modifier = intelligence_modifier
        self.charisma_modifier = charisma_modifier

        # Speed determines how far you can move while traveling. 
            # This includes traveling for both adventuring (out of combat) and during encounters (in combat).
        self.speed = speed

        # Language determines the common language used by the race. This would indicate the character can read, write and speak in this language.
        self.language = language

        # Any extra information related to the race.
        self.racial_abilities = racial_abilities
        self.description = description

        ### Will eventually want to add some kind of subclass system to this that inherits certain traits from the parent class but overwrites others.

dwarf = Race(
# General Information
    race_name="Dwarf"
    , adult_age=50
    , lifespan=400
    , size="Medium"
    , speed=30
    , language=["Common", "Dwarvish"]
    , description="Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal."
    ,racial_abilities=["Battleaxe proficiency"
      ,"Handaxe Proficiency"
      ,"Light Hammer Proficiency"
      ,"Warhammer Proficiency"
      ,"Artisan's Tools Proficiency (smith/brewer/mason)"
      ,{"Stonecunning":"Whenever making a 'History' check related to stonework, you are considered proficient in 'History' and can add double your proficiency bonus to the check."}
      ]

# Ability Modifiers
    ,strength_modifier=0
    ,dexterity_modifier=0
    ,constitution_modifier=2
    ,wisdom_modifier=0
    ,intelligence_modifier=0
    ,charisma_modifier=0
    
)

elf = Race(
    race_name='elf',
    adult_age=100,
    lifespan=750,
    size='Medium',
    speed=30,
    language=['Common','Elvish'],
    description='Elves are a magical people of otherworldy grace, living in the world but not entirely a part of it. They live in places of etheral beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic art and atristry, music and poetry , and the good things of the world',
    racial_abilities=['Darkvision','Keen Senses', 'Fey Ancestry', 'Trance'],

    # Modifiers
    strength_modifier=0,
    dexterity_modifier=2,
    constitution_modifier=0,
    wisdom_modifier=2,
    intelligence_modifier=0,
    charisma_modifier=0

)

halfling = Race(
    race_name='Halfling',
    adult_age=20,
    lifespan=200,
    size='Small',
    speed=25,
    language=['Common','Halfling'],
    description='The diminutive halflings surivie in a world full of larger creatures by avoiding notice or, barring that, avoiding offense. Standing about 3 feet tall, they appear relatively harmless and so have managed to survive for centuries in the shadow of empires and on the edges of wars and political strife. They are inclined to be stout, weighing between 40 and 50 pounds.',
    racial_abilities=['Lucky','Brave','Halfling Nimbleness'],

    # Modifiers
    strength_modifier=0,
    dexterity_modifier=2,
    constitution_modifier=0,
    wisdom_modifier=0,
    intelligence_modifier=0,
    charisma_modifier=0

)

human = Race(
    race_name='Human',
    adult_age=18,
    lifespan=80,
    size='Medium',
    speed=30,
    language=['Common'],
    description='',
    racial_abilities=[],

    # Modifiers
    strength_modifier=1,
    dexterity_modifier=1,
    constitution_modifier=1,
    wisdom_modifier=1,
    intelligence_modifier=1,
    charisma_modifier=1
)
