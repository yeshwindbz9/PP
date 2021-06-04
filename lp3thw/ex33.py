#while loops 
n = int(input('Number of elements : '))
x = []
i = 0
while i<n:
	e = input(f'Enter the element no {i} : ')
	x.append(e)
	i+=1
print('printing your list...')
j = 0
while j<n:
	print(f'Enter the element no {j} : {x[j]}')
	j+=1