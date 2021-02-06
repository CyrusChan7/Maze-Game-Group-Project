import random


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
            inner_list.append(file_content[pos].strip("\n"))
            #append inner list array to game map array 
            game_map.append(inner_list)
        
        #assign private var _filename the contents of game map array
        self._filename = game_map
        # print(f"DEBUG: file_content {self._filename}")


    #getter for maze structure
    @property
    def display(self):
        for row in self._filename:
            print(row)
    

    def check(self, line_number_, column_number_):
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
        if line_number_ > 19:   
            line_number_ = 19
        elif line_number_ < 0:
            line_number_ = 0

        if column_number_ > 19:
            column_number_ = 19
        elif column_number_ < 0:
            column_number_ = 0

        #The 0 enters the string in the index assigned to the line_number_
        #column_number_ is the index parsing through the string
        if (self._filename[line_number_][0][column_number_] == " "):
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
        #create random column number between 0 - 19.
        rand_col_num = random.randint(0, 19)
        
        #Call check function to determine if empty space
        while self.check(rand_line_num, rand_col_num) != True:
            #if the position is not empty, keep the running the loop until empty position is found
            rand_line_num = random.randint(0, 19)
            rand_col_num = random.randint(0, 19)
            
        #return the empty position
        return (rand_line_num, rand_col_num)


if __name__ == "__main__":
    gamers = Maze("maze.txt")
    # gamers.display
    # print(gamers.check(0,1))
    print(gamers.find_random_spot())       # True Empty
    # print(gamers.check(4, 8))
    # print(gamers.check(10, 2))
    # print(gamers.check(8, 3))
    # print(gamers.check(0, 4))
