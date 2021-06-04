from sys import argv
script , file = argv

print(f'Going to truncate the file {file}')
print('Press return to continue')
print('hit ctrl-c to interrupt')
input(">")

print('opening file {}'.format(file))
f = open(file,'w+')
print('truncating the file , say goodbye!')
f.truncate()
print('Writing three lines to file...')
l1 = input('Enter line one\n')
l2 = input('Line two\n')
l3 = input('line three\n')
l  =f'''
{l1}
{l2}
{l3}
'''
f.seek(0)
f.write(l)
print(f'filename : {file} ')
print('contents')
f.seek(0)
print(f.read())
print('closing the file')
f.close()
