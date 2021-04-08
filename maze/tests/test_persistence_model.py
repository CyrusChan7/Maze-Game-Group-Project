import pytest
from models.persistence import Persistence
from models.score import Score

def test_instance():
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
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert hasattr(the_data, 'get_scores')

def test_get_scores():
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert the_data.get_scores() == {"name": "john","score": 500,"date": "test_date"}

def test_to_csv_exists():
    the_score = Score()
    the_score.from_dict({"name": "john","score": 500,"date": "test_date"})
    the_data = Persistence(the_score)

    assert hasattr(the_data, 'to_csv')

    #no need to test whether csv works in this case due to how pytest works
    #no error checking needed as Score would need error checks instead

    #example error checking
    # def test_two():
    # try:
    #     with pytest.raises(ValueError):
    #         the_player = Player("", 100, 20, 20)
    # except:
    #     assert False