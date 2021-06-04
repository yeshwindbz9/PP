from sys import argv
script , file = argv
f = open(file)
print('opening and reading the file now...')
print(f'file name : {file}')
print(f.read())
