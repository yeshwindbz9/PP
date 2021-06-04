#copying stuff
from sys import argv
from os.path import exists
script , frmFile , toFile = argv
print(f'Copying from file {frmFile} to file {toFile}..')
t = open(frmFile)
data = t.read()
print(f'the output file is {len(data)}bits long')
print(f'does the file {toFile} exist ? {exists(toFile)}')
y = open(toFile,'w+')
y.write(data)
if exists(tofile):
	print('File copied sucessfully...')
else:
	print('Error copying...')
