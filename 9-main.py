#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City


print("")
all_states = storage.all(State).values()
print(all_states)
#for state in all_states:
#    if state.id == '421a55f4-7d82-47d9-b54c-a76916479552':
#        for city in state.cities:
#            print("Find the city {} in the state {} with state_id {}".format(city.name, state.name, state.id))
