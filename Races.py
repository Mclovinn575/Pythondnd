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


template = Race(
# General Information
    # Race Name
    ""
    # Adult Age of this Race
    , 0

    # Average Lifespan of this Race
    , 100

    # Size of this race
    , "Medium"

    # Speed of this Race
    , 30

    # Languages of this Race
    , ["Common",]

    # Description of the Race
    , ""

    # Inherint traits of this Race. May grant additional perks/abilities.
    ,[]

# Ability Modifiers
    # Strength Modifier
    ,0
    # Dexterity Modifier
    ,0
    # Constitution Modifier
    ,0
    # Wisdom Modifier
    ,0
    # Intelligence Modifier
    ,0
    # Charisma Modifier
    ,0
    
    
    
)

Dwarf = Race(
# General Information
    # Race Name
    "Dwarf"
    # Adult Age of this Race
    , 50

    # Average Lifespan of this Race
    , 400

    # Size of this race
    , "Medium"

    # Speed of this Race
    , 30

    # Languages of this Race
    , ["Common", "Dwarvish"]

    # Description of the Race
    , "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal."

    # Inherint traits of this Race. May grant additional perks/abilities.
    ,["Battleaxe proficiency"
      ,"Handaxe Proficiency"
      ,"Light Hammer Proficiency"
      ,"Warhammer Proficiency"
      ,"Artisan's Tools Proficiency (smith/brewer/mason)"
      ,{"Stonecunning":"Whenever making a 'History' check related to stonework, you are considered proficient in 'History' and can add double your proficiency bonus to the check."}
      ]


# Ability Modifiers
    # Strength Modifier
    ,0
    # Dexterity Modifier
    ,0
    # Constitution Modifier
    ,2
    # Wisdom Modifier
    ,0
    # Intelligence Modifier
    ,0
    # Charisma Modifier
    ,0
    
    
    
)


Human = Race(
# General Information
    # Race Name
    "Human"
    # Adult Age of this Race
    , 20

    # Average Lifespan of this Race
    , 80

    # Size of this race
    , "Medium"

    # Speed of this Race
    , 30

    # Languages of this Race
    , ["Common",]

    # Description of the Race
    , ""

    # Inherint traits of this Race. May grant additional perks/abilities.
    ,[]
# Ability Modifiers
    # Strength Modifier
    ,0
    # Dexterity Modifier
    ,0
    # Constitution Modifier
    ,0
    # Wisdom Modifier
    ,0
    # Intelligence Modifier
    ,0
    # Charisma Modifier
    ,0
    
    
    
)

