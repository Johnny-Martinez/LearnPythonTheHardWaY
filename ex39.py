<<<<<<< HEAD
#Create a mapping of state to abbreviation
=======
#Mapping of state and abbreviation
>>>>>>> dab3a55bcfce049117a226a8d7773707e33ad12e
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

<<<<<<< HEAD
#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco'
    'MI': 'Detroit'
    'FL': 'Jacksonville'
}

#Add some more cities
=======
#basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add more cities
>>>>>>> dab3a55bcfce049117a226a8d7773707e33ad12e
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_' * 10)
<<<<<<< HEAD
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
=======
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])
>>>>>>> dab3a55bcfce049117a226a8d7773707e33ad12e

#print some states
print('_' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

<<<<<<< HEAD
#Do it by using the state then cities dict
=======
#do it by using the state then cities dict
>>>>>>> dab3a55bcfce049117a226a8d7773707e33ad12e
print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

<<<<<<< HEAD
#Print every state abbreviation
print('_' * 10)
for state abbrev in states.items():
    print("%s state is abbreviated %s" % (state, abbrev))
=======
#print every state abbreviation
print('_' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s " % (state, abbrev))

#print every city in state
print('_' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

#Now do both at the same time
print('_' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('_' * 10)
#Safely get an abbreviation by stat that might not be there.
state = states.get('Texas', None)

if not state:
    print("Sorry no Texas")

#Get a city with a default value
city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is: %s " % city)

>>>>>>> dab3a55bcfce049117a226a8d7773707e33ad12e
