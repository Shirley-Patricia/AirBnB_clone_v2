#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, escape, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
