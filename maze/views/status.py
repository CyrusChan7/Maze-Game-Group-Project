from models.maze import Maze
import pygame

class StatusView:
    """
    Displays the win or lose message at the end of a game, and closes the window after 
    a 3 second delay

    :param screen_: pygame window passed from Game view
    :type screen_: pygame surface
    """
    def __init__(self, screen_):
      self._screen = screen_
      
    def display_message(self, msg_):
      """
      Displays the message that is passed from the game view or player view

      :param msg_: Message letting player know if they have lost or won the game
      :type msg_: string
      """
      status_surface = pygame.Surface((400, 40))
      status_surface.set_colorkey((255, 255, 255))
      self._screen.blit(status_surface.convert(), (200, 790))
      
      font = pygame.font.Font(None, 30)
      color = pygame.Color('white')
      status = font.render(msg_, True, color)
      self._screen.blit(status, (200, 790))
      
      pygame.display.flip()
      
      # wait for 3 seconds and then close the screen
      pygame.time.wait(3000)
