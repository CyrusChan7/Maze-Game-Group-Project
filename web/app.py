from flask import Flask, request, render_template, redirect
from web_models.score_manager import ScoreManager
from web_models.score import Score
import json
import os

app = Flask(__name__)

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
os.chdir(dir_name)      # Change to the location of where the script is located

filepath = os.path.join("..", "maze", "datacsv.csv")
score_manager = ScoreManager(filepath)

@app.route('/')
def list_scores():

    score_manager = ScoreManager(filepath)
    scores_list = score_manager.get_scores()
    scores_list.sort(key=lambda x: x.score, reverse=True)    # Sort the list of dictionary score values, from highest to lowest

    return render_template("list.html", allScores=scores_list)

@app.route('/clear', methods=['POST'])      # Button will redirect to this route and clear all saved high scores
def clear_scores():
    score_manager = ScoreManager(filepath)
    score_manager.to_csv(filepath)

    return "", 204

if __name__ == "__main__":
    app.run()
