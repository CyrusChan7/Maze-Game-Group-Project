import pytest
from models.score import Score
from models.player import Player


def test_instance():
    """
    Test whether the class is instantiated properly
    """
    test_player_model = Player()

    assert hasattr(test_player_model, "_backpack")
    test_player_model._backpack = ["T", "D"]
    assert test_player_model._backpack == ["T", "D"]

    assert hasattr(test_player_model, "_x_coordinate")
    # set x coordinate
    test_player_model._x_coordinate = 12
    # check x coordinate value set correctly
    assert test_player_model._x_coordinate == 12

    assert hasattr(test_player_model, "_y_coordinate")
    # set y coordinate
    test_player_model._y_coordinate = 10
    # check y coordinate value set correctly
    assert test_player_model._y_coordinate == 10

def test_backpack():
    """
    Tests if the backpack exists and is able to store items
    """
    test_player_model = Player()

    assert type(test_player_model.__class__.backpack) == property

    assert hasattr(test_player_model, "backpack")
    test_player_model.backpack = ["T", "D"]
    assert test_player_model.backpack == ["T", "D"]

def test_x_coordinate():
    """
    Tests whether x_coordinate property exists, and tests whether or not the getter and setter functions correctly
    """
    test_player_model = Player()
    
    assert type(test_player_model.__class__.x_coordinate) == property

    assert hasattr(test_player_model, "x_coordinate")
    test_player_model.x_coordinate = 12
    assert test_player_model.x_coordinate == 12
    
def test_y_coordinate():
    """
    Tests whetherh y_coordinate property exists, and tests the setter and getter of the y_coordinate property
    """
    test_player_model = Player()
    
    assert type(test_player_model.__class__.y_coordinate) == property
    
    assert hasattr(test_player_model, "y_coordinate")
    test_player_model.y_coordinate = 12
    assert test_player_model.y_coordinate == 12

def test_append_to_backpack_exists():
    """
    Tests whether the player backpack gets correctly appended to
    """
    test_player_model = Player()
    
    assert hasattr(test_player_model, "append_to_backpack")
    
    test_player_model.append_to_backpack("E")
    assert test_player_model.backpack == ["E"]

    test_player_model.append_to_backpack("T")
    assert test_player_model.backpack == ["E", "T"]
    
    test_player_model.append_to_backpack("P")
    assert test_player_model.backpack == ["E", "T", "P"]
