import entity
from Factories import enemy_factory
from EnemyTypes import easy_goblin
from EnemyTypes import easy_ogre
from EnemyTypes import easy_troll
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
  """ Will randomly construct an easy enemy type that can be used in the game.
  Attributes:
    None
  """

  def create_random_enemy(self):
    """Randomly creates one of the easy enemies"""
    randomizer = random.randint(1, 3)
    if randomizer == 1:
      return(easy_goblin.EasyGoblin())
    elif randomizer == 2:
      return(easy_ogre.EasyOgre())
    elif randomizer == 3:
      return(easy_troll.EasyTroll())
