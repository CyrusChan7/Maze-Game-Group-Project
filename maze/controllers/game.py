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
        Initializes maze, and view attributes
        """
        self._maze = Maze("maze.txt") 
        self._maze.put_objects_on_map()
        
        self._view = GameView(self._maze)
    
    
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
