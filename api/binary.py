from flask import Blueprint, Flask, app, jsonify
import random

from py import apipkg

binary_api = Blueprint('binary_api', __name__,
                       url_prefix = '/api/binary')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = apipkg(binary_api)

@app.route('/api/binary', methods=['GET'])
def randomBinary ():
    #Generate a random integer
    randomNumber = random.randint(0,32)

    #Convert to binary
    binaryRepresentation = bin(randomNumber)[2:]

    responseData = {
        'randomNumber': randomNumber,
        'binaryRepresentation': binaryRepresentation
    }

    return jsonify(responseData)

if __name__ == "__main__":
    app.run(debug=True)