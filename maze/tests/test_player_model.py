import pytest
from models.score import Score
from models.player import Player


def test_instance():
    # Player constructor does not take any params
    test_player_model = Player()

    assert hasattr(test_player_model, "_backpack")
    test_player_model._backpack = ["T", "D"]
    assert test_player_model._backpack == ["T", "D"]

    assert hasattr(test_player_model, "_x_coordinate")
    # set x coordinate
    test_player_model._x_coordinate = 12
    assert test_player_model._x_coordinate == 12

    assert hasattr(test_player_model, "_y_coordinate")
    # set y coordinate
    test_player_model._y_coordinate = 10
    assert test_player_model._y_coordinate == 10

def test_backpack():
    test_player_model = Player()

    assert type(test_player_model.__class__.backpack) == property

    assert hasattr(test_player_model, "backpack")
    test_player_model.backpack = ["T", "D"]
    assert test_player_model.backpack == ["T", "D"]

def test_x_coordinate():
    test_player_model = Player()
    
    assert type(test_player_model.__class__.x_coordinate) == property

    assert hasattr(test_player_model, "x_coordinate")
    test_player_model.x_coordinate = 12
    assert test_player_model.x_coordinate == 12
    
def test_y_coordinate():
    test_player_model = Player()
    
    assert type(test_player_model.__class__.y_coordinate) == property
    
    assert hasattr(test_player_model, "y_coordinate")
    test_player_model.y_coordinate = 12
    assert test_player_model.y_coordinate == 12

def test_append_to_backpack_exists():
    test_player_model = Player()
    
    assert hasattr(test_player_model, "append_to_backpack")
    
    test_player_model.append_to_backpack("E")
    assert test_player_model.backpack == ["E"]

    test_player_model.append_to_backpack("T")
    assert test_player_model.backpack == ["E", "T"]
    
    test_player_model.append_to_backpack("P")
    assert test_player_model.backpack == ["E", "T", "P"]