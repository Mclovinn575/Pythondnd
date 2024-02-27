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
                 ,strength_bonus
                 ,dexterity_bonus
                 ,constitution_bonus
                 ,wisdom_bonus
                 ,intelligence_bonus
                 ,charisma_bonus
                 ) -> None:

        
        # Establishes the name 
        self.name = race_name
        
        # The age entry determines when a memeber of a race becomes an 'Adult'
        self.adult_age = adult_age
        self.lifespan = lifespan

        # Large Size = 8+ feet tall
        # Medium Size = 4 - 8 feet tall
        # Small Size = 2 - 4 feet tall
            # A characters size can affect different gameplay rules and can cause the character to react differently to certain actions.
        self.size = size

        # Attribute bonuss
         
        self.strength_bonus = strength_bonus
        self.dexterity_bonus = dexterity_bonus
        self.constitution_bonus = constitution_bonus
        self.wisdom_bonus = wisdom_bonus
        self.intelligence_bonus = intelligence_bonus
        self.charisma_bonus = charisma_bonus

        # Speed determines how far you can move while traveling. 
            # This includes traveling for both adventuring (out of combat) and during encounters (in combat).
        self.speed = speed

        # Language determines the common language used by the race. This would indicate the character can read, write and speak in this language.
        self.language = language

        # Any extra information related to the race.
        self.racial_abilities = racial_abilities
        self.description = description

        ### Will eventually want to add some kind of subclass system to this that inherits certain traits from the parent class but overwrites others.








# =============================================================================
# Establish Race Defaults
# =============================================================================

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

# Ability bonus
    ,strength_bonus=0
    ,dexterity_bonus=0
    ,constitution_bonus=2
    ,wisdom_bonus=0
    ,intelligence_bonus=0
    ,charisma_bonus=0
    
)

elf = Race(
    race_name='Elf',
    adult_age=100,
    lifespan=750,
    size='Medium',
    speed=30,
    language=['Common','Elvish'],
    description='Elves are a magical people of otherworldy grace, living in the world but not entirely a part of it. They live in places of etheral beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic art and atristry, music and poetry , and the good things of the world',
    racial_abilities=['Darkvision','Keen Senses', 'Fey Ancestry', 'Trance'],

    # bonus
    strength_bonus=0,
    dexterity_bonus=2,
    constitution_bonus=0,
    wisdom_bonus=2,
    intelligence_bonus=0,
    charisma_bonus=0

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

    # bonus
    strength_bonus=0,
    dexterity_bonus=2,
    constitution_bonus=0,
    wisdom_bonus=0,
    intelligence_bonus=0,
    charisma_bonus=0

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

    # bonus
    strength_bonus=1,
    dexterity_bonus=1,
    constitution_bonus=1,
    wisdom_bonus=1,
    intelligence_bonus=1,
    charisma_bonus=1
)

dragonborn = Race(
    race_name='Dragonborn',
    adult_age=15,
    lifespan=80,
    size='Medium',
    speed=30,
    language=['Common','Draconic'],
    description='',
    racial_abilities=['Draconic Ancestry','Breath Weapon','Damage Resistance',],

    # bonus
    strength_bonus=2,
    dexterity_bonus=0,
    constitution_bonus=0,
    wisdom_bonus=0,
    intelligence_bonus=0,
    charisma_bonus=1
)

gnome = Race(
    race_name='Gnome',
    adult_age=40,
    lifespan=450,
    size='Small',
    speed=25,
    language=['Common','Gnomish'],
    description='',
    racial_abilities=['Darkvision','Gnome Cunning'],

    # bonus
    strength_bonus=0,
    dexterity_bonus=0,
    constitution_bonus=0,
    wisdom_bonus=0,
    intelligence_bonus=2,
    charisma_bonus=0
)

halfelf = Race(
    race_name='Half Elf',
    adult_age=20,
    lifespan=180,
    size='Medium',
    speed=30,
    language=['Common','Elvish','Extra Language'],
    description='',
    racial_abilities=['Darkvision','Fey Ancestry','Skill Versatility'],

    # bonus
    # ================ For a Half Elf they are allowed to select 2 +1 ability bonuses =====================
    # Default set to +1 Int and +1 Dex
    strength_bonus=0,
    dexterity_bonus=1,
    constitution_bonus=0,
    wisdom_bonus=0,
    intelligence_bonus=1,
    charisma_bonus=2
)

halforc = Race(
    race_name='Half-Orc',
    adult_age=14,
    lifespan=75,
    size='Medium',
    speed=30,
    language=['Common','Orc'],
    description='',
    racial_abilities=['Darkvision','Menacing','Relentless Endurance','Savage Attacks'],

    # bonus
    strength_bonus=2,
    dexterity_bonus=0,
    constitution_bonus=1,
    wisdom_bonus=0,
    intelligence_bonus=0,
    charisma_bonus=0
)

tiefling = Race(
    race_name='Tiefling',
    adult_age=18,
    lifespan=100,
    size='Medium',
    speed=30,
    language=['Common','Infernal'],
    description='',
    racial_abilities=['Darkvision','Hellish Resistance','Infernal Legacy'],

    # bonus
    strength_bonus=0,
    dexterity_bonus=0,
    constitution_bonus=0,
    wisdom_bonus=0,
    intelligence_bonus=1,
    charisma_bonus=2
)