five_things_str = 'zero one two three'
print(five_things_str)
five_things = five_things_str.split(' ')

while len(five_things)!= 6:
	e = input('Enter a new element : ')
	five_things.append(e)

print(" ".join(five_things))
print(five_things)

