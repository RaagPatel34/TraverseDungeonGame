import entity
from Factories import enemy_factory
from EnemyTypes import goblin
from EnemyTypes import ogre
from EnemyTypes import troll
import random

class ExpertFactory(enemy_factory.EnemyFactory):
  """ Will randomly construct an difficult enemy type that can be used in the game.
  Attributes:
    None
  """

  def create_random_enemy(self):
    """Randomly creates one of the difficult enemies"""
    randomizer = random.randint(1, 3)
    if randomizer == 1:
      return(goblin.Goblin())
    elif randomizer == 2:
      return(ogre.Ogre())
    elif randomizer == 3:
      return(troll.Troll())
