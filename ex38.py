states = {
	'O':'OR',
	'Florida':'FL',
	'California':'CA',
	'New york':'NY',
	'Michigan':'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*30
print "NY state has :", cities['NY']
print "OR state has :",cities ['OR']
print '-' * 30
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 30
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-'* 30
for state,abbrev in states.items():
	print "%s is abbreviated %s " % (state,abbrev) 
	
print '-' * 30
for abbrev,city in cities.items():
	print "%s has the city %s " % (abbrev,city)
	
print '-' * 30
for state , abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state,abbrev,cities[abbrev])
print '-' * 30
state = states.get("Texas",None)
print state

if not state:
	print "sorry,no Texas"
	
city = cities.get('TX','Does not exist')
city1= cities.get('CA','does\'t exist')

print "the city for the state 'TX' is :%s" % city
print city1


i='abc'
j=i.join('defg')
print j




