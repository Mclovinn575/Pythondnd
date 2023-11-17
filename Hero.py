import random
import Armory

class Character:
    default_weapon = Armory.fists
    def __init__(self, name, hp,  weapon = default_weapon) -> None:
        self.name = name
        self.weapon = weapon
        self.maxhp = hp
        self.hp = hp
        self.weapon =  weapon

    def Attack(self, target):
        damage = random.randint(self.weapon.minDmg, self.weapon.maxDmg)
        target.hp -= damage
        print(f"{self.name} swings {self.weapon.name} for {damage} damage!")
    
    def Heal(self):
        heal = random.randint(1,5)
        newhp = self.hitpoints =+ heal
        print(f"Healed {newhp}")

    def Drop(self):
        self.weapon = self.default_weapon
        print(f"{self.name} is now using {self.weapon.name}")


    def Equip(self, item):
        self.weapon = item
        item_name = item.name
        print(f"{self.name} equips a(n) {item_name}")


