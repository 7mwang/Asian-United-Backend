from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random-binary', methods=['GET'])
def random_binary():
    # Generate a random integer
    random_number = random.randint(0, 32)

    # Convert the random number to binary
    binary_representation = bin(random_number)[2:]

    response_data = {
        'random_number': random_number,
        'binary_representation': binary_representation
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)