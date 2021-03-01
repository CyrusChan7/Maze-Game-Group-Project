class Player:
    """
    Represents a player that will play in the maze game
    
    :param filename: Name of file being passed to create structure of the maze
    :param filename: string
    """

    def __init__(self):
        self._backpack = []     # Initialize empty list for backpack of items picked up along the way
        self._x_coordinate = 0  # Track location (x and y coordinates) of player in the maze
        self._y_coordinate = 0
    
    @property
    def backpack(self):
        return self._backpack

    # This is required because list append doesn't work in setters
    @backpack.setter
    def backpack(self, value):
        self._backpack.append(value)

        
    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, value):
        self._x_coordinate = value
        #self.coordinate_check()

    @property
    def y_coordinate(self):
        return self._y_coordinate
    
    @y_coordinate.setter
    def y_coordinate(self, value):
        self._y_coordinate = value
        #self.coordinate_check()
    