class Map:
  """ Creates the board that will be used throughout the game
  Attributes:
    _instance: instance of the class
    _initialized: initialization of the class
  """

  _instance = None
  _initialized = False

  def __new__(cls):
    """if the map hasn’t been constructed, then it constructs and stores it in the instance class variable and returns it. If it has, then just returns the instance."""
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance
  
  def __init__(self):
    """Initializes the map"""
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True

  def load_map(self, map_num):
    """Passes in an integer to choose which of the three maps to choose from. Then it resets map and revealed and loads in the new map 
    """
    file = open(f"map{map_num}.txt")
    map = []
    for row in file:
      list = []
      for item in row:
        if item != ' ' and item != '\n':
          list.append(item)
      map.append(list)
    self._map = map
    revealed = []
    for i in range(len(map)):
      revealed1 = []
      for j in range(len(map[0])):
        revealed1.append(False)
      revealed.append(revealed1)
    self._revealed = revealed

  
  def __getitem__(self, row):
    """Returns the specified row in the map"""
    return(self._map[row])

  def __len__(self):
    """Returns number of rows in the map"""
    return(len(self._map))

  def show_map(self, loc):
    """returns the map as a string in the format of a 5x5 matrix of 
characters where revealed locations are the characters from the map, unrevealed locations are ‘x’s, and the hero’s location is a ‘*’"""
    hero_map = "" 
    row_count = -1
    for row in self._revealed:
      row_count += 1
      column_count = 0
      for column in row:
        if row_count == loc[0] and column_count == loc[1]:
          hero_map += "* "
        elif column == False:
          hero_map += ("x ")
        elif column == True:
          hero_map += (self._map[row_count][column_count] + " ")
        column_count += 1
      hero_map += ("\n")
    return(hero_map)
    
    
  def reveal(self, loc):
    """Sets specified location on map to True"""
    self._revealed[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    """Overwrites the character in the map list at the specified location with an n"""
    self._map[loc[0]][loc[1]] = "n"
