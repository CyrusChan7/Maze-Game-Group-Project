from flask import Flask, request, render_template
from web_models.score_manager import ScoreManager
from web_models.score import Score
import json
import os

app = Flask(__name__)

abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)
os.chdir(dir_name)
filepath = os.path.join("..", "maze", "datacsv.csv")

score_manager = ScoreManager(filepath)

@app.route('/')
def list_scores():
    score_manager = ScoreManager(filepath)
    scores_list = score_manager.get_scores()

    return render_template("list.html", allScores=scores_list)

@app.route('/api/list')
def list_all_scores():
    return {"scores": score_manager.get_scores()}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    try:
        "get the JSON data of the request, containing a new object to add"
        data = request.get_json()
        score = Score(data['name'], data['score'], data['date'])
        score_manager.add_score(score)
        return "", 204
    except:
        return "Invalid data provided.", 400


@app.route('/api/list', methods=["DELETE"])
def delete_score():
    try:
        "get the JSON data of the request, containing an object to delete"
        data = request.get_json()
        score_manager.remove_score(data['name'])
        return "", 204
    except:
        return "Invalid data provided.", 400

if __name__ == "__main__":
    app.run()
    