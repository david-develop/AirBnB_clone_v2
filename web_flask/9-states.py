#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(self):
    """Close storage session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """display a HTML page with all states and cities"""
    all_states = storage.all(State).values()
    return render_template('9-states.html', all_states=all_states, state_id=None)


@app.route('/states/<id_str>', strict_slashes=False)
def cities_by_state(id_str):
    """display a HTML page with all states and cities"""
    all_states = storage.all(State)
    obj_key = "State." + id_str
    if obj_key in all_states:
        state = all_states[obj_key]
        return render_template('9-states.html', state=state, state_id=id_str)
    else:
        return render_template('9-states.html', state=None, state_id=id_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
