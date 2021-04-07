from datetime import datetime
import json

class Score:
    def __init__(self):
        """
        This Model represents a Player's score

        """
        self._player_name = "Yves"
        # change this score value to calculate score based on how fast the player finishes
        self._score = 0
        self._current_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    @property
    def player_name(self):
        return self._player_name

    @property
    def score(self):
        return self._score

    @score.setter
    @property
    def score(self, new_score):
        self._score = new_score
        
    @property
    def date(self):
        return self._current_date
    

    def to_dict(self):
        #Return a dictionary version of Player instance
        return {
            "name": self._player_name,
            "score": self._score,
            "date": self._current_date
        }


    def from_dict(self, inst_dict):
        #Return a new instance containing data from json data 
        self._player_name = inst_dict["name"]
        self._score = int(inst_dict["score"])
        self._current_date = inst_dict["date"]
