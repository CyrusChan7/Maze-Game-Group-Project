from pygame.constants import KEYDOWN, K_w
import pygame.locals
import sys
from models.maze import Maze
from views.game import GameView

class GameController:
    """
    Controls the player object
    """
    def __init__(self):
        """
        Initializes maze, view attribute, player time, and player backpack
        """
        self._maze = Maze("maze.txt")
        self._maze.put_objects_on_map()
        
        self._view = GameView(self._maze)
        self._player_time = 0
        self._player_backpack = []

    # getter for player time
    @property
    def player_time(self):
        return self._player_time

    # getter for player backpack
    @property
    def player_backpack(self):
        return self._player_backpack

    def get_user_input(self):
        """
        Identifies events occuring while the game runs and calls appropriate methods
        """
        run_game = True 
        while run_game:
            self._view.refresh()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                    run_game = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self._view.move_player("UP")
                    elif event.key == pygame.K_a:
                        self._view.move_player("LEFT")
                    elif event.key == pygame.K_s:
                        self._view.move_player("DOWN")
                    elif event.key == pygame.K_d:
                        self._view.move_player("RIGHT")
            
            self._player_time = self._view.player_time
            self._player_backpack = self._view.player_backpack
