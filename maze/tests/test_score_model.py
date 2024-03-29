import pytest
from models.score import Score
from models.player import Player


def test_instance():
    """
    Test whether the Player class is instantiated properly
    """
    the_score = Score()
    
    assert hasattr(the_score, '_player_name')
    assert type(the_score._player_name) == str
    the_score._player_name == ""
    
    assert hasattr(the_score, '_score')
    assert type(the_score._score) == int
    assert the_score._score == 0
    
    assert hasattr(the_score, '_current_date')
    assert type(the_score._current_date) == str
    
def test_player_name_property():
    """
    Tests whether player_name property exists
    """
    the_score = Score()
    
    assert hasattr(the_score, 'player_name')
    assert type(the_score.__class__.player_name) == property
    
def test_score_property():
    """
    Tests whether score property exists
    """
    the_score = Score()
    
    assert hasattr(the_score, 'score')
    assert type(the_score.__class__.score) == property

def test_date_property():
    """
    Tests whether date property exists
    """
    the_score = Score()

    assert hasattr(the_score, 'date')
    assert type(the_score.__class__.date) == property

def test_to_dict():
    """
    Tests whether method to_dict exists
    """
    the_score = Score()

    assert hasattr(the_score, 'to_dict')
    assert the_score.to_dict() == {"name": "", "score": 0, "date": "test-date"}

def test_from_dict():
    """
    Tests whether or not the data is received correctly from the dictionary 
    """
    the_score = Score()

    assert hasattr(the_score, 'from_dict')
    the_score.from_dict({"name": "John", "score": 100, "date": 'test-date2'})
    
    assert the_score.player_name == "John"
    assert the_score.score == 100
    assert the_score.date == "test-date2"
