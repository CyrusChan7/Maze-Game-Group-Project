from views.status import StatusView
from models.maze import Maze
from models.score import Score
import pygame

class PlayerView:
    """
    Renders a screen for the maze game

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
        self._player_picture = pygame.image.load("images/player.png")
        self._player_sprite = pygame.transform.scale(self._player_picture, (40, 40))
        self._screen.blit(self._player_sprite, (0, 0))
        
    def move_player(self, new_x, new_y):
        """
        Does work for Game view of moving the player Sprite to the new position

        :param new_x: new x pos for the player Sprite
        :type new_x: int
        
        :param new_y: new y pos for the player Sprite
        :type new_y: int
        
        :return: None
        """
        #Get the player instance
        p = self._maze.player
        
        #save the old x & y coordinates
        old_x = p.x_coordinate
        old_y = p.y_coordinate
            
        #update the new x & y coordinates
        p.x_coordinate = new_x
        p.y_coordinate = new_y

        #determine item and pick it up
        if self._maze.is_item(new_x, new_y) == True:
            item = self._maze.game_map[new_x][new_y]
            if item != 'G' and item != 'E':
                p.append_to_backpack(item)

        #update player position and delete old position
        self._maze.game_map[old_x][old_y] = ' '
        self._maze.game_map[new_x][new_y] = 'G'

        #show player on screen
        self._screen.blit(self._player_sprite, (p.y_coordinate*40, p.x_coordinate*40))
        square_surface = pygame.Surface((40, 40))
        square_surface.set_colorkey((255, 255, 255))
        self._screen.blit(square_surface.convert(), (old_y*40, old_x*40))
        
        #determine if exit has been reached
        if self._maze.is_exit(new_x, new_y) == True:
            #print(self._maze.win_or_lose())
            msg = self._maze.win_or_lose()

            #pass win or lose message to status view to display
            status_view = StatusView(self._screen) 
            status_view.display_message(msg)
            raise SystemExit(msg)
