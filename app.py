from flask import Flask, request
from backend import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    req = request.values.get('value')
    print(req)
    if insert_data(req) == 'Success':
        return 'Success'
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
