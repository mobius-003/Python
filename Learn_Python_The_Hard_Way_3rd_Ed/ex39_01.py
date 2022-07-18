#create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida': 'FL',
    'Califorina': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add som emore cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print every state abbreviation
print('_____'* 10)
for x, y in list(states.items()):
    print(f"{x} is abbreviated {y}")

#print every city in state
print('-----'* 10)
for i, j in list(cities.items()):
    print(f" ...has city {cities[i]}")

#now do both at the same time
print('   '* 10)
print('-----'* 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has city {cities[abbrev]}")
    print('  '* 10)
