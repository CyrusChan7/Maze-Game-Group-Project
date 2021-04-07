import json
import csv
from datetime import datetime
from .score import Score
import os

class ScoreManager:
    """ Simple collection of Scores """

    def __init__(self, player_file_):
        self._scores = []
        self._filename = player_file_
        self.from_csv(self._filename)

    def __len__(self):
        return len(self._scores)
    
    @property
    def scores(self):
        return self._scores

    def add_score(self, score):
        if isinstance(score, Score) == True:
            self._scores.append({
                score.name: score
            })
        else:
            raise TypeError("score item should be an instance of Score")
    
    def remove_score(self, score_name):
        del self._scores[score_name]

    def get_scores(self):
        scores_list = []
        for i in range(len(self._scores)):
            temp_key = list(self._scores[i])
            scores_list.append(self._scores[i][temp_key[0]])
        
        return scores_list
     
    def serialize(self):
        return {"scores": self.get_scores()}
    
    def to_csv(self, csv_file):
        with open(csv_file, 'w') as csvf:
            fieldnames = ["name", "score", "date"]
            writer = csv.DictWriter(csvf, fieldnames)
            writer.writeheader()
            for namescore in self.get_scores():
                writer.writerow(namescore)

    def from_csv(self, csv_file):
        try:
            with open(csv_file, 'r') as csvf:
                csv_reader = csv.reader(csvf)
                for item in csv_reader:
                    if len(item) != 0:
                        self.add_score(Score(
                            str(item[0]),
                            int(item[1]),
                            str(item[2])
                        ))
        except:
            print("Error: datacsv.csv does not exist")

    def add_to_csv(self, csv_file):
        with open(csv_file, 'a') as csvf:
            fieldnames = ["name", "score", "date"]
            writer = csv.DictWriter(csvf, fieldnames)
            writer.writeheader()
            for namescore in self.get_scores():
                writer.writerow(namescore)

if __name__ == "__main__":
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)
    
    # print(os.getcwd())
    filepath = os.path.join("..", "..", "maze", "datacsv.csv")
    #print(filepath)

    manager = ScoreManager(filepath)
    print(manager.get_scores())