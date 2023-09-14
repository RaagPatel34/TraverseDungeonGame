import abc

class Entity(abc.ABC):
  """ Creates the entities that will be used in the game
  Attributes:
    name (string): name of the entity
    _hp (int): current health points of the entity
    max_hp (int): maximum health points of the entity
  """

  def __init__(self, name, max_hp):
    """Initializes the entity"""
    self._name = name
    self._max_hp = max_hp
    self._hp = max_hp

  @property
  def name(self):
    """Gets name of entity"""
    return self._name

  @property
  def hp(self):
    """Gets health points of entity"""
    return self._hp

  def take_damage(self, dmg):
    """Allows the entity to take damage"""
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0

  def heal(self):
    """Heals the players hp to max"""
    self._hp = self._max_hp

  @abc.abstractmethod
  def attack(self, entity):
    """Creating the method that the other classes can use"""
    pass

  def __str__(self):
    """String representation of the class"""
    return (str(self._name) + "\nHP: " + str(self._hp) + "/" +
            str(self._max_hp))
