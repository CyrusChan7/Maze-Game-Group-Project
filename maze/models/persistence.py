import csv
import os

class Persistence:
    def __init__(self, player_dict):
        self._player_name = player_dict.player_name
        self._player_score = player_dict.score
        self._player_date = player_dict.date

    def get_scores(self):
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
