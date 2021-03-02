from main import Maze
from player import Player
import pygame

def new_spot(the_maze, sprite, new_x, new_y, screen, curr_x, curr_y):
    """
        Behaviour: checks if requested location is the exit
        
        :param the_maze: Line number coordinate of specified location
        :type the_maze: int
        
        :param sprite: Column number coordinate of specified location
        :type sprite: int
        
        :param new_x: Column number coordinate of specified location
        :type new_x: int
        
        :param new_y: Column number coordinate of specified location
        :type new_y: int
        
        :param screen: Column number coordinate of specified location
        :type screen: int
        
        :param curr_x: Column number coordinate of specified location
        :type curr_x: int
        
        :param curr_y: Column number coordinate of specified location
        :type curr_y: int
    
        """
    if the_maze.can_move_to(new_x, new_y) == True:
        screen.blit(sprite, (new_y*40, new_x*40))
        square_surface = pygame.Surface((40, 40))
        square_shape = pygame.draw.rect(square_surface, (0, 0, 0), (0, 0, 40, 40))
        square_surface.set_colorkey((255, 255, 255))
        screen.blit(square_surface.convert(), (curr_y*40, curr_x*40))

def main():
    game_maze = Maze("maze.txt")
    game_maze.put_objects_on_map()
    game_map = []
    with open("maze_objects_placed.txt") as f:
        file_content = f.readlines()

    for pos, line in enumerate(file_content):
        inner_list = []
        for letter in file_content[pos].strip("\n"):
            inner_list.append(letter)
        game_map.append(inner_list)
    
    player1 = Player()

    pygame.init()
    screen = pygame.display.set_mode((800, 820))
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 40)
    clock = pygame.time.Clock()
    blue = pygame.Color('white')
    timer = 120
    time_passed = 0

    pygame.display.set_caption("Brian, Sahil, Raihan, and Cyrus' Maze Game")

    player_picture = pygame.image.load("images/player.png")
    player_sprite = pygame.transform.scale(player_picture, (40, 40))
    screen.blit(player_sprite, (0,0))     # Displays the player.png

    treasure_picture = pygame.image.load("images/treasure.png")
    treasure_sprite = pygame.transform.scale(treasure_picture, (40, 40))
    
    dagger_picture = pygame.image.load("images/dagger.png")
    dagger_sprite = pygame.transform.scale(dagger_picture, (40, 40))
    
    helmet_picture = pygame.image.load("images/helmet.png")
    helmet_sprite = pygame.transform.scale(helmet_picture, (40, 40))
    
    potion_picture = pygame.image.load("images/potion.png")
    potion_sprite = pygame.transform.scale(potion_picture, (40, 40))

    block_picture = pygame.image.load("images/block.png")
    block_sprite = pygame.transform.scale(block_picture, (40, 40))

    exit_picture = pygame.image.load("images/exit.png")
    exit_sprite = pygame.transform.scale(exit_picture, (40, 40))

    for pos, x_cord in enumerate(game_map):
        for pas, y_cord in enumerate(x_cord):
            if y_cord == 'X':
                screen.blit(block_sprite, (pas*40,pos*40))
            if y_cord == 'T':
                screen.blit(treasure_sprite, (pas*40,pos*40))
            if y_cord == 'D':
                screen.blit(dagger_sprite, (pas*40,pos*40))
            if y_cord == 'H':
                screen.blit(helmet_sprite, (pas*40,pos*40))
            if y_cord == 'P':
                screen.blit(potion_sprite, (pas*40,pos*40))
            if y_cord == 'E':
                screen.blit(exit_sprite, (pas*40,pos*40))

    run_game = True
    while run_game:
        x_player = str(player1.x_coordinate)
        y_player = str(player1.y_coordinate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                new_y = int(y_player)
                new_x = int(x_player) - 1
                old_x = new_x + 1
                old_y = new_y
                if new_x >= 0:
                    game_maze.move_player([new_x, new_y])
                    new_spot(game_maze, player_sprite, new_x, new_y, screen, old_x, old_y)
            
            elif keys[pygame.K_a]:
                new_y = int(y_player) - 1
                new_x = int(x_player)
                old_x = new_x
                old_y = new_y + 1
                if new_y >= 0:
                    game_maze.move_player([new_x, new_y])
                    new_spot(game_maze, player_sprite, new_x, new_y, screen, old_x, old_y)

            elif keys[pygame.K_s]:
                new_y = int(y_player)
                new_x = int(x_player) + 1
                old_x = new_x - 1
                old_y = new_y
                if new_x <= 19:
                    game_maze.move_player([new_x, new_y])
                    new_spot(game_maze, player_sprite, new_x, new_y, screen, old_x, old_y)
                
            elif keys[pygame.K_d]:
                new_y = int(y_player) + 1
                new_x = int(x_player)
                old_x = new_x
                old_y = new_y - 1
                if new_y <= 19:
                    game_maze.move_player([new_x, new_y])
                    new_spot(game_maze, player_sprite, new_x, new_y, screen, old_x, old_y)

        timer -= time_passed
        if timer <= 0:
            print("You lost because you ran out of time!")
            quit()
        text = str(round(timer, 2)) + 's'
        txt = font.render(text, True, blue)
        screen.blit(txt, (5, 790))
        pygame.display.flip()
        time_passed = clock.tick(30) / 1000  # / 1000 to convert to seconds.

        square_surface = pygame.Surface((200, 40))
        square_shape = pygame.draw.rect(square_surface, (0, 0, 0), (0, 0, 200, 40))
        square_surface.set_colorkey((255, 255, 255))
        screen.blit(square_surface.convert(), (5, 790))

        pygame.display.update()

main()
