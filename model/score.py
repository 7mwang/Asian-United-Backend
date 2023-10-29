from flask import Flask, request, jsonify
app = Flask(__name__)

# In-memory data store for game scores
game_scores = []

@app.route('/api/scores', methods=['POST'])
def store_score():
    data = request.get_json()
    score = data.get('score')

    if score is not None and isinstance(score, int):
        game_scores.append(score)
        return jsonify(message='Score stored successfully'), 201
    else:
        return jsonify(error='Invalid score format'), 400

@app.route('/api/scores', methods=['GET'])
def get_scores():
    return jsonify(scores=game_scores)

if __name__ == '__main__':
    app.run(debug=True)
