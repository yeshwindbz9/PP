'''
stuff = {'name':'Buggati','model':'Veyron','price':'3million'}
print(stuff)
stuff['units'] = '20'
print(stuff)
'''
#mapping state to abbrev
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}
#abbrev states and their city
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}
#adding two more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#printing some cities
print('-'*10)
print("NY State has: ", cities['NY']) 
print("OR State has: ", cities['OR']) 
#printing some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
#printing by using state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']]) 
print("Florida has: ", cities[states['Florida']])
#print all abbrevs
print('-'*10)
for state, abbrev in list(states.items()): 
	print(f'{state} is abbreviated as {abbrev}')
#print all abrev and city
print('-'*10)
for state, abbrev in list(states.items()):
	print(f'{state} is abbriviated as {abbrev}')
	print(f'and has city {cities[abbrev]}')

print('-'*10)
#what if the state is not there
state = states.get('Texas')
if not state:
	print('Sorry state not present in the list')
#get a city with default value
city = cities.get('TX','Does not Exist!')
print(f'The city for the state "TX" is : {city}')


print(states.get('Texas'))
print(list(states.items()))