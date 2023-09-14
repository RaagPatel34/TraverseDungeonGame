import entity
import random

class Ogre(entity.Entity):
  """ Creates a difficult ogre enemy
  Attributes:
    name (string): name of the enemy
    _hp (int): current health points of the enemy
    max_hp (int): maximum health points of the enemy
  """

  def __init__(self):
    """Initializes the difficult ogre enemy"""
    randhp = random.randint(8, 12)
    name = "Lumbering Ogre"
    super().__init__(name, max_hp = randhp)
    self._hp = randhp

  def attack(self, entity):
    """Performs an attack against the hero"""
    attack_dmg = random.randint(6, 10)
    entity.take_damage(attack_dmg)
    return(self._name + " attacks you for " + str(attack_dmg) + " damage.")
