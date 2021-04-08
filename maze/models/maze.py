import random
from models.player import Player

class Maze:
    """
    Represents a maze game that takes in a file to create the structure of the maze

    :param filename: Name of file being passed to create structure of the maze
    :type filename: string
    """
    def __init__(self, filename_):
        """
        Initializes the player and game map attributes
        """
        self._player = Player()
        
        # Nested list
        self._game_map = []

        with open(filename_) as f:
            #read file contents
            file_content = f.readlines()
            
        #enumerate through each line in the file (position and file contents stored)
        for pos, line in enumerate(file_content):
            inner_list = []
            #append each line to inner list array
            for letter in file_content[pos].strip("\n"):
                inner_list.append(letter)
            #append inner list array to game map array 
            self._game_map.append(inner_list)

    # getter for player object
    @property
    def player(self):
        return self._player

    # getter for game_map object
    @property
    def game_map(self):
        return self._game_map
    
    def can_move_to(self, line_num_, column_num_):
        """
        Recieve a line number and column number to check if it as empty space

        :param line_number_: Number of the line in the maze (x coordinate)
        :type line_number_: int

        :param column_number_: Number of the column in the maze (y coordinate)
        :type column_number_: int

        :return: TRUE if empty space, FALSE if wall present 
        :rtype: boolean
        """

        # column_number_ is the index parsing through the string
        if self._game_map[line_num_][column_num_] != "X":
            return True     # Return true if empty space

        else:
            return False


    def find_random_spot(self):
        """
        Return a tuple of line number and column number that is a random empty space

        :return: Tuple of a line number and column number (coordinate of an empty space in the maze)
        :rtype: tuple
        """
        # create random line number between 0 - 19
        rand_line_num = random.randint(0, 19)
        # create random column number between 0 - 19
        rand_col_num = random.randint(0, 19)

        # Call check function to determine if empty space
        while self.can_move_to(rand_line_num, rand_col_num) != True:
            if self.is_exit(rand_line_num, rand_col_num) != True:
                if self.is_start(rand_line_num, rand_col_num) != True:
                    rand_line_num = random.randint(0, 19)
                    rand_col_num = random.randint(0, 19)

        # return the empty position
        return (rand_line_num, rand_col_num)


    def put_objects_on_map(self):
        """
        Randomly select 4 empty spots to place objects into the maze

        :return: None
        """
        treasures = ["T", "D", "H", "P"]  # T for Treasure, D for Dagger, H for Helmet, P for Potion
        game_mapping = self._game_map

        for i in range(4):
            # record the line and column coordinates for an empty space in the maze
            empty_line_num, empty_col_num = self.find_random_spot()

            game_mapping[empty_line_num][empty_col_num] = treasures[i]

        # creates new file that will be written to 4 times (4 random objects)
        with open("maze_objects_placed.txt", "w") as f:

            #iterates through the map and adds an object to an empty space
            for row in game_mapping:
                #this makes a new line
                row_word = ""
                #this appends maze information to the line
                for letter in row:
                    row_word += letter
                #this writes the maze row into the file
                f.write(f"{row_word}\n")

        self._game_map = game_mapping


    def is_item(self, line_num_, column_num_):
        """
        Behaviour: Checks if specified coordinates is a maze object (not empty space or wall)

        :param line_num_: Line number coordinate of specified location
        :type line_num_: int

        :param column_num_: Column number coordinate of specified location
        :type column_num_: int

        :return: TRUE if location is an object, FALSE if location is not an object (empty space or wall)
        :rtype: boolean
        """
        # check if specified location is an empty space, or a wall
        if (self._game_map[line_num_][column_num_] == " " or self._game_map[line_num_][column_num_] == "X"):
            return False     # This is either an empty space or a wall
        else:
            return True      # This is an item


    def is_exit(self, line_num_, column_num_):
        """
        Behaviour: Checks if requested location is the exit

        :param line_num_: Line number coordinate of specified location
        :type line_num_: int

        :param column_num_: Column number coordinate of specified location
        :type column_num_: int

        :return: TRUE if specified location is an exit of the maze, FALSE if the location is not an exit
        :rtype: boolean
        """
        if line_num_ == 19 and column_num_ == 19:
            return True     # The specified number is the exit
        else:
            return False    # The specified number is not the exit


    def is_start(self, line_num_, column_num_):
        """
        Behaviour: Checks if requested location is the start

        :param line_num_: Line number coordinate of specified location
        :type line_num_: int

        :param column_num_: Column number coordinate of specified location
        :type column_num_: int

        :return: TRUE if specified location is an start of the maze, FALSE if the location is not start
        :rtype: boolean
        """
        if line_num_ == 0 and column_num_ == 0:
            return True     # The specified number is the start
        else:
            return False    # The specified number is not the start


    def win_or_lose(self):
        """
        Behaviour: Determine if the player has won or lost the game by checking the length of the backpack

        :return: Message indicating if player has won or lost the game
        :rtype: string
        """
        if len(self._player.backpack) == 4:
            exit_message = "You WON - Congratulations!"
        else:
            exit_message = f"You LOST - You only collected {len(self._player.backpack)} of 4 items!"
            
        return exit_message
