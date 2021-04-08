class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name_, score_, date_):
        """
        Initializes private attributes 

        :param name_: The name of the score to add
        :type name_: string
        
        :param score_: The score of the score to add
        :type score_: int
        
        :param date_: The date associated with the score to add
        :type date_: string
        
        :return: None
        """

        if type(name_) is not str or not name_:
            raise ValueError("Invalid name.")
        
        if type(score_) is not int or score_ < 0:
            raise ValueError("Invalid score.")

        self._name = name_
        self._score = score_
        self._date = date_

    # getter for the player's name
    @property
    def name(self):
        return self._name
    
    # getter for the player's score
    @property
    def score(self):
        return self._score

    # getter for the player's date
    @property
    def date(self):
        return self._date