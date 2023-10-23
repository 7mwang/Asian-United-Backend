from flask import Flask, jsonify
import random

binary_api = Blueprint('binary_api', __name__,
                       url_prefix = '/binary')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(binary_api)

@app.route('/binary', methods=['GET'])
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