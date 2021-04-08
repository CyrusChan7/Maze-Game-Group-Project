import json
import csv
from datetime import datetime
from .score import Score
import os

class ScoreManager:
    """ 
    Simple collection of Scores 
    """
    def __init__(self, player_file_):
        """ 
        Initializes a score manager
        
        :param player_file_: CSV file passes that will be used to persist the data
        :type player_file_: filepath
        """
        self._scores = []
        self._filename = player_file_
        self.from_csv(self._filename)

    # dunder method to get number of scores being managed by the score manager 
    def __len__(self):
        return len(self._scores)
    
    # getter for the scores being managed by the score manager
    @property
    def scores(self):
        return self._scores
    
    def add_score(self, score):
        """
        Adds a score to the score manager 
        
        :param score_: Score object to be added
        :type score_: Score object

        :return: None
        """
        # Adds a score to the score manager if the score is of type score
        if isinstance(score, Score) == True:
            self._scores.append({
                score.name: score
            })
        else:
            # score passed is not of type score
            raise TypeError("score item should be an instance of Score")
    
    def remove_score(self, score_name_):
        """
        Removes a score from the Score Manager

        :param score_name_: The name assosicated with the score to remove
        :type score_name_: string
        
        :return: None
        """
        del self._scores[score_name_]
            
            
    def get_scores(self):
        """
        Returns a list of scores being managed by the score manager
        
        :return: List of all scores being managed by the score manager
        :return type: List
        """
        scores_list = []
        for i in range(len(self._scores)):
            temp_key = list(self._scores[i])
            scores_list.append(self._scores[i][temp_key[0]])

        return scores_list
     

    def serialize(self):
        """
        Returns a list of scores being managed by the score manager
        
        :return: dictionary of scores, with key "scores"
        :return type: dictionary
        """
        return {"scores": self.get_scores()}
    

    def to_csv(self, csv_file):
        """
        Save everything to a file, in CSV format
        
        :param csv_file: Path to CSV file
        :type csv_file: string
        
        :return: None
        """
        with open(csv_file, 'w') as csvf:
            writer = csv.writer(csvf)
            writer.writerow("")


    def from_csv(self, csv_file):
        """
        Load everything from the CSV file, and create a score object for each score in the CSV file
        
        :param csv_file: Path to CSV file
        :type csv_file: string
        
        :return: None
        """
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
