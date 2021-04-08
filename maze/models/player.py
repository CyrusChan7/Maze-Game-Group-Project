class Player:
    """
    Represents a player that will play in the maze game
    """
    def __init__(self):
        """
        Initializes backpack, and x, y coordinate
        """
        self._backpack = []
        self._x_coordinate = 0
        self._y_coordinate = 0
    
    # getter for Player backpack
    @property
    def backpack(self):
        return self._backpack

    # This is required because list append doesn't work in setters
    @backpack.setter
    def backpack(self, value):
        self._backpack = value
     
    # getter for player x coordinate
    @property
    def x_coordinate(self):
        return self._x_coordinate

    # setter for player x coordinate
    @x_coordinate.setter
    def x_coordinate(self, value):
        self._x_coordinate = int(value)

    # getter for player y coordinate
    @property
    def y_coordinate(self):
        return self._y_coordinate
    
    # setter for player y coordinate
    @y_coordinate.setter
    def y_coordinate(self, value):
        self._y_coordinate = int(value)


    def append_to_backpack(self, value):
        """
        Adds object in maze to backpack
        
        :param value: item to add to the backpack
        :type value: string
        """

        self._backpack.append(value)
