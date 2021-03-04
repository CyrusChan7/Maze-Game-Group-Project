from models.maze import Maze
import pygame

class MazeWallView:
    """
    Displays the maze walls

    :param maze_: maze object to be used for the view
    :type maze_: Maze
    
    :param screen_: pygame window passed from Game view
    :type screen_: pygame surface
    """
    def __init__(self, maze_, screen_):
        """
        Initializes values for maze game
        """
        self._maze = maze_
        self._screen = screen_

        #importing images as sprites
        block_picture = pygame.image.load("images/block.png")
        block_sprite = pygame.transform.scale(block_picture, (40, 40))

        exit_picture = pygame.image.load("images/exit.png")
        exit_sprite = pygame.transform.scale(exit_picture, (40, 40))

        #runs a for loop through the maze map and display sprites based on string
        for y, row in enumerate(self._maze.game_map):
            for x, col in enumerate(row):
                if col == 'X':
                    self._screen.blit(block_sprite, (x*40, y*40))
                if col == 'E':
                    self._screen.blit(exit_sprite, (x*40, y*40))
        