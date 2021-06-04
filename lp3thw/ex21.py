def add(a,b):
	print(f'addition of {a} and {b}')
	return a + b

def sub(a,b):
	print(f'subtraction of {a} and {b}')
	return a - b

def mul(a,b):
	print(f'multiplication of {a} and {b}')
	return a * b

def div(a,b):
	print(f'division of {a} and {b}')
	return a / b

x = add(2,5)
x1 = sub(2,5)
x2 = mul(2,5)
x3 = div(2,5)
print('Respective answers : {} {} {} {}'.format(x,x1,x2,x3))