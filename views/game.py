from models.maze import Maze
from models.player import Player
import pygame

class GameView:
  
    def __init__(self, maze_):
        self._maze = maze_

        pygame.init()

        self._screen = pygame.display.set_mode((800, 820))
        self._screen.fill((0, 0, 0))

        self._font = pygame.font.Font(None, 40)
        self._clock = pygame.time.Clock()
        self._color = pygame.Color('white')
        self._timer = 120
        self._time_passed = 0

        pygame.display.set_caption("Brian, Sahil, Raihan, and Cyrus' Maze Game")

        self._player_picture = pygame.image.load("images/player.png")
        self._player_sprite = pygame.transform.scale(self._player_picture, (40, 40))
        self._screen.blit(self._player_sprite, (0, 0))     # Displays the player.png

        self._treasure_picture = pygame.image.load("images/treasure.png")
        self._treasure_sprite = pygame.transform.scale(self._treasure_picture, (40, 40))

        self._dagger_picture = pygame.image.load("images/dagger.png")
        self._dagger_sprite = pygame.transform.scale(self._dagger_picture, (40, 40))

        self._helmet_picture = pygame.image.load("images/helmet.png")
        self._helmet_sprite = pygame.transform.scale(self._helmet_picture, (40, 40))

        self._potion_picture = pygame.image.load("images/potion.png")
        self._potion_sprite = pygame.transform.scale(self._potion_picture, (40, 40))

        self._block_picture = pygame.image.load("images/block.png")
        self._block_sprite = pygame.transform.scale(self._block_picture, (40, 40))

        self._exit_picture = pygame.image.load("images/exit.png")
        self._exit_sprite = pygame.transform.scale(self._exit_picture, (40, 40))

        for pos, x_cord in enumerate(self._maze.game_map):
            for pas, y_cord in enumerate(x_cord):
                if y_cord == 'X':
                    self._screen.blit(self._block_sprite, (pas*40, pos*40))
                if y_cord == 'T':
                    self._screen.blit(self._treasure_sprite, (pas*40, pos*40))
                if y_cord == 'D':
                    self._screen.blit(self._dagger_sprite, (pas*40, pos*40))
                if y_cord == 'H':
                    self._screen.blit(self._helmet_sprite, (pas*40, pos*40))
                if y_cord == 'P':
                    self._screen.blit(self._potion_sprite, (pas*40, pos*40))
                if y_cord == 'E':
                    self._screen.blit(self._exit_sprite, (pas*40, pos*40))
        
        pygame.display.flip()
        pygame.display.update()            

    def move_player(self, action_):
        """
        Behaviour: Use other determined functions to move the player around the maze
        and update the map. Controls what happens when the player moves to the exit - determine if win/lose and quit.
        Also controls if player moves over item - addes to backpack

        :return: None
        """
        
        #Get the player instance
        p = self._maze.player
        
        xloc = p.x_coordinate
        yloc = p.y_coordinate
        new_x = 0
        new_y = 0
        
        
        #fix logic and add checks to make sure player does not go out of index range
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


        if self._maze.can_move_to(new_x, new_y) == True:
            #save the old x & y coordinates
            old_x = p.x_coordinate
            old_y = p.y_coordinate
            
            #update the new x & y coordinates
            p.x_coordinate = new_x
            p.y_coordinate = new_y

            if self._maze.is_exit(new_x, new_y) == True:
                self._maze.game_map[old_x][old_y] = ' '
                self._maze.game_map[new_x][new_y] = 'G'
                print(self._maze.win_or_lose())
                raise SystemExit("User has reached the end of the maze")

            if self._maze.is_item(new_x, new_y) == True:
                item = self._maze.game_map[new_x][new_y]
                if item != 'G':
                    p.append_to_backpack(item)
                    # self._maze.game_map[old_x][old_y] = ' '
                    # self._maze.game_map[new_x][new_y] = 'G'

            self._maze.game_map[old_x][old_y] = ' '
            self._maze.game_map[new_x][new_y] = 'G'

    def refresh(self, xloc_, yloc_):
        p = self._maze.player
                
        self._screen.blit(self._player_sprite, (p.y_coordinate*40, p.x_coordinate*40))
        square_surface = pygame.Surface((40, 40))
        square_shape = pygame.draw.rect(square_surface, (0, 0, 0), (0, 0, 40, 40))
        square_surface.set_colorkey((255, 255, 255))
        self._screen.blit(square_surface.convert(), (yloc_*40, xloc_*40))
        
        self._timer -= self._time_passed
        if self._timer <= 0:
            print("You lost because you ran out of time!")
            raise SystemExit("You lost because you ran out of time!")
            
        text = str(round(self._timer, 2)) + 's'
        txt = self._font.render(text, True, self._color)
        self._screen.blit(txt, (5, 790))
        pygame.display.flip()
        time_passed = self._clock.tick(30) / 1000  # / 1000 to convert to seconds.
                
        square_surface = pygame.Surface((200, 40))
        square_shape = pygame.draw.rect(square_surface, (0, 0, 0), (0, 0, 200, 40))
        square_surface.set_colorkey((255, 255, 255))
        self._screen.blit(square_surface.convert(), (5, 790))

        pygame.display.update()        