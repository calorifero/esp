from flask import Flask, request, render_template
from backend import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    req = str(request.values.get('value'))
    if insert_data(req) == 'Success':
        return 'Success'
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
