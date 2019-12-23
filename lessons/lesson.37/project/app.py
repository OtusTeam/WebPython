import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_page():
    return '<h1>Hello world!</h1>'


if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    print('Desired host:', host)
    app.run(debug=True, host=host, port=5000)
