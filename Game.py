import GameMenu
import Character
import Races
import Armory
import character_Classes


# while True:
#     GameMenu.Menu()

# verified that information is able to be pulled correctly from associated files in this format.
hero = Character.Character(
    name='Michael',
    race=Races.human,
    characterClass=character_Classes.fighter
)

hero.Stow(Armory.dagger)
hero.Stow(Armory.flail)
Character.statBlock(hero)





