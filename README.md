Maze Game Instructions and Information

Maze game creators: Brian, Sahil, Raihan, and Cyrus

Please take your time to go through this ^_____^


The project structure:

    -controllers directory:
        responsible for the movement of the player, and identifying events that happen in the game then calling the appropriate methods
        
    -views directory:
        responsible for the display of the map, countdown timer, and the loading of the sprite images. Each item has it's own sub view responsible for displaying the item, created by the Game View
        
    -models directory:
        responsible for handling the logic of the game map data. Such as whether or not a player can move to a certain location, the placing of items randomly (and ensuring that the item is placed within map boundaries and not on top of walls), determining whether or not a location has an item, determining whether or not a location is an exit, and determining whether or not the player has won.

Note: Image trademarks are property of their respective owners. Creators of this Maze game do not claim ownership.


Programs required:

    -Python 3
    -Visual Studio Code
    -Windows Terminal (optional)


Dependencies (install using 'pip install x', where x is the name of the library listed below):

    -pygame


How to run the code:

    -After installing the above programs and the pygame library, execute main.py to start the game


How to control the game:

    -W to move up
    -A to move left
    -S to move down
    -D to move right

Note: Player can NOT go through walls or exit the game map boundaries.


How to win the maze game:

    -The player must pick up all 4 items and reach the exit before 60 seconds. Should the 60 seconds timer run out
    or the exit is reached before all 4 items are picked up, the player loses.
