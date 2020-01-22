#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City
from models.place import Place

print("")
all_places = storage.all(Place).values()
#for state in all_states:
#    if state.id == '421a55f4-7d82-47d9-b54c-a76916479552':
#        for city in state.cities:
#            print("Find the city {} in the state {} with state_id {}".format(city.name, state.name, state.id))
for place in all_places:
    print("Name: {} -> Description: {}, id: {}".format(place.name, place.description, place.id))
