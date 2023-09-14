import abc

class EnemyFactory(abc.ABC):
  """ Creates the enemy factory class
  Attributes:
    None
  """

  @abc.abstractmethod
  def create_random_enemy(self):
    """Creates the method that will be used in beginner/expert factory"""
    pass
