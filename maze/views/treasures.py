from models.maze import Maze
import pygame

class TreasuresView:
    """
    Displays treasure Sprites at random positions

    :param maze: maze object to be used for the view
    :type maze: Maze
    
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
        treasure_picture = pygame.image.load("images/treasure.png")
        treasure_sprite = pygame.transform.scale(treasure_picture, (40, 40))

        dagger_picture = pygame.image.load("images/dagger.png")
        dagger_sprite = pygame.transform.scale(dagger_picture, (40, 40))

        helmet_picture = pygame.image.load("images/helmet.png")
        helmet_sprite = pygame.transform.scale(helmet_picture, (40, 40))

        potion_picture = pygame.image.load("images/potion.png")
        potion_sprite = pygame.transform.scale(potion_picture, (40, 40))


        #runs a for loop through the maze map and display sprites based on string
        for y, row in enumerate(self._maze.game_map):
            for x, col in enumerate(row):
                if col == 'T':
                    self._screen.blit(treasure_sprite, (x*40, y*40))
                if col == 'D':
                    self._screen.blit(dagger_sprite, (x*40, y*40))
                if col == 'H':
                    self._screen.blit(helmet_sprite, (x*40, y*40))
                if col == 'P':
                    self._screen.blit(potion_sprite, (x*40, y*40))
