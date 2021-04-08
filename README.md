Maze Game Instructions and Information

Maze game creators: Brian, Sahil, Raihan, and Cyrus

Please take your time to go through this ^_____^

The Maze game comes with two applications:
1) Maze Game
2) Web API - show highscores
*Needs to be run on seperate command lines*
NOTE: The web server should be turned on first!

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
    -Windows Terminal
    -A web browser

NOTE: Only add dependencies once a virtual environment has been created, as to not interfere with global packages.
Dependencies (install using 'pip install x', where x is the name of the library listed below):

    -pygame
    -pytest (only if you want to run our unit testing files)
    -Flask

Web API:

    -Once the player has won the game, they will be given a score (calculated by time remaining * 25)        
        -Hence the faster the that the player finishes the game, the higher the score that they will receive
    -The player's username, score, and date stamp of completion will be persisted to CSV file first, and then rendered by the webpage through the web API
    -Visiting the website will show all saved user data (from CSV file), sorted from highest to lowest on the webpage

How to run the web server:

    -After installing the above programs and the above dependencies:
        -Execute app.py in the web directory to start the Web API then visit (localhost:5000/ to view the web page)- this will show all the scores

        -Refresh the webpage after winning the maze game to see your username and how you rank amongst others

How to run the maze game:

    -After installing the above programs and the above dependencies:
        -Execute main.py to start the Maze game - this will open a GUI where the user will be prompted to enter a username for the game


How to control the game:

    -W to move up
    -A to move left
    -S to move down
    -D to move right

Note: Player will NOT be able to go through walls or exit the game map boundaries.
NOTE

How to win the maze game:

    -The player must pick up all 4 items and reach the exit before 60 seconds. Should the 60 seconds timer run out
    or the exit is reached before all 4 items are picked up, the player loses.

    