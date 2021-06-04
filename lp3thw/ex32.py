x = []
n = int(input("Enter the number of elements in your list : "))

for element in range(n):
	e = input(f"Enter the element {element} : ")
	x.append(e)
print(x)

s = 'Mary had a little lamb'
print(s)
x = s.split(' ')
print(x)
print(' '.join(x))