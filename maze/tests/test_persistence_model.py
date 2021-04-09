import pytest
from models.persistence import Persistence
from models.score import Score

def test_instance():
    """
    Test whether the class is instantiated properly
    """
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert hasattr(the_data, '_player_name')
    assert the_data._player_name == "john"

    assert hasattr(the_data, '_player_score')
    assert the_data._player_score == 500

    assert hasattr(the_data, '_player_date')
    assert the_data._player_date == "test_date"

def test_get_scores_exists():
    """
    Tests whether or not get_scores() exists
    """
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert hasattr(the_data, 'get_scores')

def test_get_scores():
    """
    Tests whether the data is received from the dictionary properly
    """
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert the_data.get_scores() == {"name": "john","score": 500,"date": "test_date"}

def test_to_csv_exists():
    """
    Tests whether or not the method to_csv() exists
    """
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert hasattr(the_data, 'to_csv')
