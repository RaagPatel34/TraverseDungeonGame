import map
import entity
import random

class Hero(entity.Entity):
  """ Creates the hero that will be used in the game
  Attributes:
    location (list): current location of the hero on the map
    name (string): name of the hero
    _hp (int): current health points of the hero
    max_hp (int): maximum health points of the hero
  """

  def __init__(self, name):
    """Initializes the entity"""
    super().__init__(name, max_hp = 25)
    self._hp = self._max_hp
    self._loc = [0, 0]

  @property
  def loc(self):
    """returns location of hero"""
    return self._loc

  def attack(self, entity):
    """Allows hero to attack the enemy"""
    attack_dmg = random.randint(2, 5)
    entity.take_damage(attack_dmg)
    return(self._name + " attacks " + str(entity.name) + " for " + str(attack_dmg) + " damage.")

  def go_north(self):#row
    """Allows hero to go up one"""
    map1 = map.Map()
    self._loc[0] -= 1
    if self._loc[0] < 0:
      self._loc[0] += 1
      return("x")
    return(map1[self._loc[0]][self._loc[1]])
      
  def go_south(self):#row
    """Allows hero to go down one"""
    map1 = map.Map()
    self._loc[0] += 1
    if self._loc[0] > len(map1)-1:
      self._loc[0] -= 1
      return("x")
    return(map1[self._loc[0]][self._loc[1]])#character/string
    
  def go_west(self):#column
    """Allows hero to go left one"""
    map1 = map.Map()
    self._loc[1] -= 1
    if self._loc[1] < 0:
      self._loc[1] += 1
      return("x")
    return(map1[self._loc[0]][self._loc[1]])
    
  def go_east(self):#column
    """Allows hero to go right one"""
    map1 = map.Map()
    self.loc[1] += 1
    print(self.loc[1])
    if self._loc[1] > len(map1[0])-1:
      self._loc[1] -= 1
      return("x")
    return(map1[self._loc[0]][self._loc[1]])
