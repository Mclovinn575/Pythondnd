# This page will store all of the available playable character classes.
import random
class Character_Class:

    def __init__(self,
                 name,
                 hit_die,
                 base_hp
                 ) -> None:


        self.name = name
        self.hit_die = hit_die
        self.base_hp = base_hp
        pass


barbarian = Character_Class("Barbarian",(random.randint(1,12)), 12)
print(barbarian.name)
print(barbarian.hit_die)