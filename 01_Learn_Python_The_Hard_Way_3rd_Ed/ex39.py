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

#print out some cities
print('--1-- '* 10)
print("NY state has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some stateså
print('--2--'* 10)
print("Michigan's abreviation is: ", states['Michigan'])
print("Florida's abreviation is: ", states["Florida"])

#do it by using  the state then cities dict
print('--3--'* 10)
print("Michigan has : ", cities[states['Michigan']])
print("Florida has : ", cities[states["Florida"]])

#print every state abbreviation
print('--4--'* 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('--5--'* 10)
for abbrev, city in list(cities.items()):
    print(f" has city {cities[abbrev]}")

#now do both at the same time
print('    '* 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has city {cities[abbrev]}")

print(' \/ '* 10)
#safely get a abbreviation by state that might not be there
state = states.get('Tex')

if not state:
    print("Sorry, no TX. ")
#get a city a default value
city = cities.get('TX','Does Not Exist')
print(f" The city for the state of Texas is: {city}")
