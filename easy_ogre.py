import entity
import random

class EasyOgre(entity.Entity):
  """ Creates an easy ogre enemy
  Attributes:
    name (string): name of the enemy
    _hp (int): current health points of the enemy
    max_hp (int): maximum health points of the enemy
  """

  def __init__(self):
    """Initializes the easy ogre enemy"""
    randhp = random.randint(3, 5)
    name = "Ogre"
    super().__init__(name, max_hp = randhp)
    self._hp = randhp

  def attack(self, entity):
    """Performs an attack against the hero"""
    attack_dmg = random.randint(1, 4)
    entity.take_damage(attack_dmg)
    return(self._name + " attacks you for " + str(attack_dmg) + " damage.")
