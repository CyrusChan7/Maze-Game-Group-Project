import csv
import os

class Persistence:
    """
    Controls the persistance of data

    :param player_dict: Score object passed from main.py
    :type player_dict: Score object
    """
    def __init__(self, player_dict):
        #access player name, score, and date from dictionary passed
        self._player_name = player_dict.player_name
        self._player_score = player_dict.score
        self._player_date = player_dict.date

    def get_scores(self):
        #return a dictionary representation of the player
        return {
            "name": self._player_name,
            "score": self._player_score,
            "date": self._player_date
        }

    def to_csv(self):
        with open("datacsv.csv", 'a') as csvf:
            fieldnames = ["name", "score", "date"]
            writer = csv.DictWriter(csvf, fieldnames)
            writer.writerow(self.get_scores())
