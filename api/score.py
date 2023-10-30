from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

score_api = Blueprint("score_api", __name__, url_prefix = "/api/scores")
api = Api(score_api)

# In-memory data store for game scores
game_scores = []

class ScoreAPI(Resource):
    def get(self):
        return jsonify(scores=game_scores)

    def post(self):
        data = request.get_json()
        score = data.get('score')

        if score is not None and isinstance(score, int):
            game_scores.append(score)
            return jsonify(message='Score stored successfully'), 201
        else:
            return jsonify(error='Invalid score format'), 400

api.add_resource(ScoreAPI, '/')

