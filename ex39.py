#Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco'
    'MI': 'Detroit'
    'FL': 'Jacksonville'
}

#Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#Do it by using the state then cities dict
print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#Print every state abbreviation
print('_' * 10)
for state abbrev in states.items():
    print("%s state is abbreviated %s" % (state, abbrev))