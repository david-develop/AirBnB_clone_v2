#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
all_states = storage.all(State)
states_name_id = {value.id: value.name for (key, value) in all_states.items()}
sort_list = dict(sorted(states_name_id.items(), key = lambda x : x[1]))

@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with all states and cities"""
    return render_template('7-states_list.html', class_n="States",
                           all_states=sort_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
