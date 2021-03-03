import pygame
import sys
from models.maze import Maze
from models.player import Player
from views.game import GameView

class GameController:
  
  def __init__(self):
    """
    Call the classmethod to load all students from the CSV
    """
    self._maze = Maze("maze.txt") 
    self._maze.put_objects_on_map()
    self._view = GameView(self._maze)
  
  
  def get_user_input(self):                 
    run_game = True
    
    #Set player to starting position
    self._view.refresh(0, 0) 
    
    while run_game:

        for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run_game = False
                break

            keys = pygame.key.get_pressed()

            old_xloc = self._maze.player.x_coordinate
            old_yloc = self._maze.player.x_coordinate

            action = ""                
            if keys[pygame.K_w]:
                action = "UP"
            elif keys[pygame.K_a]:
                action = "LEFT"                              
            elif keys[pygame.K_s]:
                action = "DOWN"                                 
            elif keys[pygame.K_d]:
                action = "RIGHT"                              

            self._view.move_player(action)
                               
            self._view.refresh(old_xloc, old_yloc)
