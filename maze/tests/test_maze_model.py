import pytest
from models.player import Player
from models.maze import Maze

def test_instance():
    the_maze = Maze('test_maze.txt')
    
    assert hasattr(the_maze, '_player')
    assert type(the_maze._player) == Player
    
    assert hasattr(the_maze, '_game_map')
    assert type(the_maze._game_map) == list
    
def test_player_property():
    the_maze = Maze('test_maze.txt')
    
    assert hasattr(the_maze, 'player')
    assert type(the_maze.__class__.player) == property
    
def test_game_map_property():
    the_maze = Maze('test_maze.txt')
    
    assert hasattr(the_maze, 'game_map')
    assert type(the_maze.__class__.game_map) == property

def test_can_move_to():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'can_move_to')
    assert the_maze.can_move_to(0, 2) == True
    assert the_maze.can_move_to(18, 19) == False

def test_find_random_spot():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'find_random_spot')

def test_put_objects_on_map():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'put_objects_on_map')

def test_is_item():
    the_maze = Maze('test_maze.txt')
    hasattr(the_maze, 'is_item')

def test_is_exit():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'is_exit')
    assert the_maze.is_exit(19, 19) == True
    assert the_maze.is_exit(4, 5) == False

def test_is_start():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'is_start')
    assert the_maze.is_start(0, 0) == True
    assert the_maze.is_start(4, 5) == False

def test_win_or_lose():
    the_maze = Maze('test_maze.txt')
    assert hasattr(the_maze, 'win_or_lose')

    the_maze._player.backpack = [1,2,3,4]
    assert the_maze.win_or_lose() == "You WON - Congratulations!"
    
    the_maze._player.backpack = [0]
    assert the_maze.win_or_lose() == "You LOST - You only collected 1 of 4 items!"

    the_maze._player.backpack = [0, 2]
    assert the_maze.win_or_lose() == "You LOST - You only collected 2 of 4 items!"

    the_maze._player.backpack = [0, 3, 5]
    assert the_maze.win_or_lose() == "You LOST - You only collected 3 of 4 items!"
