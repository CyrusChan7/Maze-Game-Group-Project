from views.status import StatusView
from views.player import PlayerView
from views.treasures import TreasuresView
from views.mazewall import MazeWallView
from models.maze import Maze
from models.player import Player
import pygame

class GameView:
    """
    This view displays the game, and creates the sub views for other "things" in the gamae

    :param maze: maze object to be used for the view
    :type maze: Maze
    """
    def __init__(self, maze_):
        """
        Initializes values for maze game
        """
        self._maze = maze_

        pygame.init()

        #creates a screen and gives it a black background
        self._screen = pygame.display.set_mode((800, 820))
        self._screen.fill((0, 0, 0))

        #sets up the timer
        self._font = pygame.font.Font(None, 40)
        self._clock = pygame.time.Clock()
        self._color = pygame.Color('white')
        self._timer = 60
        self._time_passed = 0

        #maze game title caption
        pygame.display.set_caption("Brian, Sahil, Raihan, and Cyrus' Maze Game")

        self._mazewall_view = MazeWallView(self._maze, self._screen)
        
        self._treasures_view = TreasuresView(self._maze, self._screen)
        
        self._player_view = PlayerView(self._maze, self._screen)
        
        self._status_view = StatusView(self._screen)

    def move_player(self, action_):
        """
        Recieves an action from the game controller (direction to move), and then tells the Player view to
        move the player Sprite

        :param action_: String passed from controller indicating direction to move player
        :type action_: string
        
        :return: None
        """
        #Get the player instance
        p = self._maze.player
        
        xloc = p.x_coordinate
        yloc = p.y_coordinate
        new_x = 0
        new_y = 0

        #determines what key was pressed and updates the player coordinates
        if action_ == "UP":
            new_x = xloc - 1
            new_y = yloc
        elif action_ == "DOWN":
            new_x = xloc + 1
            new_y = yloc
        elif action_ == "LEFT":
            new_x = xloc
            new_y = yloc - 1
        elif action_ == "RIGHT":
            new_x = xloc
            new_y = yloc + 1

        #also checks for map boundaries so that player cannot exit the map
        if new_x < 0 or new_x > 19 or new_y < 0 or new_y > 19:
            return None

        #move and update the players to a new location on screen
        if self._maze.can_move_to(new_x, new_y) == True:
            self._player_view.move_player(new_x, new_y)

        pygame.display.update() #added here

    def refresh(self):
        """
        Displays amount of time left before game ends
        """
        self._timer -= self._time_passed
        print(self._timer)

        square_surface = pygame.Surface((200, 40))
        square_surface.set_colorkey((255, 255, 255))
        self._screen.blit(square_surface.convert(), (5, 790))

        text = str(round(self._timer, 2)) + 's'
        txt = self._font.render(text, True, self._color)
        self._screen.blit(txt, (5, 790))
        pygame.display.flip()

        if self._timer <= 0:
            self._screen.blit(square_surface.convert(), (5, 790))
            msg = "You LOSE - Ran out of time!"
            #pass status view display message 
            self._status_view.display_message(msg)
            raise SystemExit(msg)

        self._time_passed = self._clock.tick(30) / 1000  # / 1000 to convert to seconds.

    @property
    def player_time(self):
        return self._timer
