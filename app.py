from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask(__name__)


ROOT_ENDPOINT_MESSAGE = "Welcome to the simple expression solver app! :)\n Try calling the /solve endpoint."


@app.route('/', methods=['GET'])
def index():
    return ROOT_ENDPOINT_MESSAGE


@app.route('/solve', methods=['POST'])
def solve():
    try:
        data = request.json
        response = {
            'result': eval(data['expression'])
        }
        return jsonify(response), HTTPStatus.OK
    except:
        response = {
            'error': 'Failed parsing request payload! Expected application/json content type'
        }
        return jsonify(response), HTTPStatus.BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
