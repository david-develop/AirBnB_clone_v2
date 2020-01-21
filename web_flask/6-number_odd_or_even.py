#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Define endpoint / and return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Define endpoint /hbnb and return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Define endpoint /c and return C + text"""
    msj = text.replace('_', ' ')
    return 'C %s' % msj


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """Define endpoint /python and return python + text"""
    if text != "is cool":
        msj = text.replace('_', ' ')
        return 'Python %s' % msj
    return 'Python is cool'


@app.route('/number/<int:n>')
def number(n):
    """show the post with the given number"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def render_templ(n):
    """display a HTML page only if n is an integer and render given number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def render_odd_even(n):
    """display a HTML page only if n is an integer and render given number
    if is even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
