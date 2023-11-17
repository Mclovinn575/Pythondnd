
slash = "'Slashing'"
blunt = "'Blunt'"
pierce = "'Piercing'"
simple = "simple"
martial = "martial"


class Weapon:
    
    def __init__(self, name, damageType, minDmg, maxDmg, category, is_ranged):
            self.name = name
            self.damageType = damageType
            self.minDmg = minDmg
            self.maxDmg = maxDmg
            self.category = category
            self.is_ranged = is_ranged

# Simple Melee Weapons

fists = Weapon(
    name= "Fists",
    damageType= blunt,
    minDmg= 1,
    maxDmg= 4,
    category = simple,
    is_ranged=False
)
dagger = Weapon(
    name= "Dagger",
    damageType= slash,
    minDmg = 1,
    maxDmg = 4,
    category= simple,
    is_ranged=False
)

club = Weapon(
    name= "Club",
    damageType= blunt,
    minDmg=1,
    maxDmg=4,
    category=simple,
    is_ranged=False
)

greatclub = Weapon(
    name= "Greatclub",
    damageType= blunt,
    minDmg=1,
    maxDmg=8,
    category= simple,
    is_ranged=False
)

handaxe = Weapon(
    name= "Handaxe",
    damageType= slash,
    minDmg=1,
    maxDmg=4,
    category= simple,
    is_ranged=False
)

javelin = Weapon(
    name= "Javelin",
    damageType= pierce,
    maxDmg=6,
    minDmg=1,
    category= simple,
    is_ranged=False
)

light_hammer = Weapon(
    name = "Light Hammer",
    damageType= blunt,
    minDmg=1,
    maxDmg=4,
    category= simple,
    is_ranged=False
)

mace = Weapon(
    name= "Mace",
    damageType= blunt,
    minDmg=1,
    maxDmg=6,
    category= simple,
    is_ranged=False
)

quarterstaff = Weapon(
    name= "Quarterstaff",
    damageType= blunt,
    maxDmg=6,
    minDmg=4,
    category= simple,
    is_ranged=False
)

sickle = Weapon(
    name= "Sickle",
    damageType= slash,
    minDmg=1,
    maxDmg=4,
    category= simple,
    is_ranged=False
)

spear = Weapon(
    name= "Spear",
    damageType= pierce,
    minDmg=1,
    maxDmg=6,
    category= simple,
    is_ranged=False
)

# Simple Ranged Weapons

crossbow_light = Weapon(
    name="Light Crossbow",
    damageType=pierce,
    minDmg=1,
    maxDmg=8,
    category=simple,
    is_ranged=True
)

dart = Weapon(
    name="Dart",
    damageType=pierce,
    minDmg=1,
    maxDmg=4,
    category=simple,
    is_ranged=True
)

shortbow = Weapon(
      name="Shortbow",
      damageType=pierce,
      minDmg=1,
      maxDmg=6,
      category=simple,
      is_ranged=True
)

sling = Weapon(
      name="Sling",
      damageType=blunt,
      minDmg=1,
      maxDmg=4,
      category=simple,
      is_ranged=True
)

# Adding Martial Range Weapons

blowgun = Weapon(
      name="Blowgun",
      damageType= pierce,
      minDmg=1,
      maxDmg=1,
      category=martial,
      is_ranged=True
)

crossbow_hand = Weapon(
      name="Hand Crossbow",
      damageType=pierce,
      minDmg=1,
      maxDmg=6,
      category=martial,
      is_ranged=True
)

crossbow_heavy = Weapon(
      name="Heavy Crossbow",
      damageType=pierce,
      minDmg=1,
      maxDmg=10,
      category=martial,
      is_ranged=True
)

longbow = Weapon(
      name="Longbow",
      damageType=pierce,
      minDmg=1,
      maxDmg=8,
      category=martial,
      is_ranged=True
)

net = Weapon(
      name="Net",
      damageType="",
      minDmg=0,
      maxDmg=0,
      category=martial,
      is_ranged=True
)

# Adding Martial Melee Weapons
