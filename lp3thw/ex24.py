print('Practising everything')
print('this is newline and\n \t this is new tab ')

poem = '''
what am i to you he asks
you are every hope i've ever had
in a human form i replied..
'''
print('------------------------------')
print(poem)
print('------------------------------')

five = 10-2+3-6
print(f'this should be five : {five}')

def secret_formula(started):
	beans = started*500
	jars = beans/1000
	crates = jars/100
	return beans,jars,crates

start_point = 1000
beans,jars,crates = secret_formula(start_point)

print('with start point of {}'.format(start_point))
print(f'We would have {beans} jelly beans {jars} jars and {crates} crates..')

start_point/=10
formula = secret_formula(start_point)

print('we will now have {} beans {} jars and {} crates..'.format(formula))
