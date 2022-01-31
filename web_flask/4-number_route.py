#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    return "C %s" % escape(text.replace('_', " "))


@app.route('/python/(<text>)', strict_slashes=False)
def pyth(text='is_cool'):
    return "Python %s" % escape(text.replace('_', " "))


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    return '%d is a number' % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')