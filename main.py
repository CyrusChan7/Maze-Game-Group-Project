import random
from player import Player

class Maze:
    """
    Represents a maze game that takes in a file to create the structure of the maze
    
    :param filename: Name of file being passed to create structure of the maze
    :param filename: string
    """
    def __init__(self, filename_):
        game_map = []
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
            game_map.append(inner_list)
        
        #assign private var _game_map the contents of game map array
        self._game_map = game_map
        self._player_x = 0
        self._player_y = 0
        self._player_back = []

    #getter for maze structure
    @property
    def display(self):
        #put barrier on top of maze
        print("_" * 22)
        for row in self._game_map:
            #put | on left side of the maze to be the barrier 
            row_word = "|"
            for letter in row:
                row_word += letter
            #put | on right side of the maze to be the barrier 
            print(row_word, end="| \n")
        #put barrier on bottom of maze
        #this works 2 out of 4 times
        print("‾" * 22)
    
    @property
    def player_location(self):
        return self._player_x, self._player_y
    
    @property
    def game_map(self):
        return self._game_map


    def can_move_to(self, line_num_, column_num_):
        """
        Behaviour: Recieve a line number and column number to check if it as empty space
        
        :param line_number_: Number of the line in the maze (x coordinate)
        :param line_number_: int
        
        :param column_number_: Number of the column in the maze (y coordinate)
        :param column_number_: int
        
        :return: TRUE if empty space, FALSE if wall present 
        :rtype: boolean
        """
        #Ensure that the user doesn't go out of bounds
        if line_num_ > 19:   
            line_num_ = 19
        elif line_num_ < 0:
            line_num_ = 0

        if column_num_ > 19:
            column_num_ = 19
        elif column_num_ < 0:
            column_num_ = 0

        #The 0 enters the string in the index assigned to the line_number_
        #column_number_ is the index parsing through the string
        if (self._game_map[line_num_][column_num_] != "X"):
            return True     # Return true if empty space
        else:
            return False    # Return false if wall present

    
    def find_random_spot(self):
        """
        Behaviour: Return a tuple of line number and column number that is an empty space
        
        :return: Tuple of a line number and column number (coordinate of an empty space in the maze)
        :rtype: tuple
        """
        #create random line number between 0 - 19 
        rand_line_num = random.randint(0, 19)
        #create random column number between 0 - 19
        rand_col_num = random.randint(0, 19)
        
        #Call check function to determine if empty space
        while self.can_move_to(rand_line_num, rand_col_num) != True:
            #if the position is not empty, keep the running the loop until empty position is found
            rand_line_num = random.randint(0, 19)
            rand_col_num = random.randint(0, 19)
            
        #return the empty position
        return (rand_line_num, rand_col_num)


    def put_objects_on_map(self):
        """
        Behaviour: Randomly select 4 empty spots to place objects into the maze

        :return: None
        """
        objects = ["T", "D", "H", "P"]  # T for Treasure, D for Dagger, H for Helmet, P for Potion
        game_mapping = self._game_map
        
        for i in range(4):
            #creates new file that will be written to 4 times (4 random objects)
            with open("maze_objects_placed.txt", "w") as f:
                #record the line and column coordinates for an empty space in the maze
                empty_line_num, empty_col_num = self.find_random_spot()
                #adds object to the coordinates found for empty space in the maze
                
                if empty_line_num == 0 and empty_col_num == 0: #make sure that object not placed where player starts the game
                    empty_line_num = 1
                
                game_mapping[empty_line_num][empty_col_num] = objects[i]

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
        Behaviour: Returns true if specified coordinates is a random item (not empty space or wall)
    
        :param line_num_: Line number coordinate of specified location
        :type line_num_: int
        
        :param column_num_: Column number coordinate of specified location
        :type column_num_: int
        
        :return: TRUE if location is an object, FALSE if location is not an object (empty space or wall)
        :type: boolean
        """
        #check if specified location is an empty space, or a wall
        if (self._game_map[line_num_][column_num_] == " " or self._game_map[line_num_][column_num_] == "X"):
            return False     # This is either an empty space or a wall
        else:
            return True      # This is an item


    def is_exit(self, line_num_, column_num_):
        """
        Behaviour: checks if requested location is the exit
        
        :param line_num_: Line number coordinate of specified location
        :type line_num_: int
        
        :param column_num_: Column number coordinate of specified location
        :type column_num_: int
        
        :return: TRUE if specified location is an exit of the maze, FALSE if the location is not an exit
        :type: boolean
        """
        if line_num_ == 19 and column_num_ == 19:
            return True     # The specified number is the exit
        else:
            return False    # The specified number is not the exit

    
    def move_player(self, player_loc):
        """
        Behaviour: Use other determined functions to move the player around the maze
        and update the map. Controls what happens when the player moves to the exit - determine if win/lose and quit.
        Also controls if player moves over item - addes to backpack

        :return: None
        """
        #player location = [x,y]
        new_x = player_loc[0] #x
        new_y = player_loc[1] #y
        old_x = self._player_x
        old_y = self._player_y

        if self.can_move_to(new_x, new_y) == True:
            Player.x_coordinate = new_x
            Player.y_coordinate = new_y
            self._player_x = new_x
            self._player_y = new_y

            if self.is_exit(new_x, new_y) == True:
                self._game_map[old_x][old_y] = ' '
                self._game_map[new_x][new_y] = 'G'
                print(self.win_or_lose())
                quit()

            if self.is_item(new_x, new_y) == True:
                item = self._game_map[new_x][new_y]
                if item != 'G':
                    self._player_back.append(item)
                Player.backpack = self._player_back
                self._game_map[old_x][old_y] = ' '
                self._game_map[new_x][new_y] = 'G'

            self._game_map[old_x][old_y] = ' '
            self._game_map[new_x][new_y] = 'G'


    def win_or_lose(self):
        """
        Behaviour: Determine if the player has won or lost the game by checking the length of the backpack

        :return: Message indicating if player has won or lost the game
        :rtype: string
        """
        if len(Player.backpack) == 4:
            exit_message = "You won, congratulations!" 
            return exit_message
        else:
            exit_message = "You lost because you didn't collect all of the items!"
            return exit_message
