#functions and file
from sys import argv
script , file = argv

def printFile(t):
	print(t.read())

def rewind(t):
	t.seek(0)

def printLine(linecount,t):
	print(linecount,t.readline())

t = open(file)
printFile(t)
rewind(t)

linecount = 1
printLine(linecount,t)
printLine(linecount+1,t)
printLine(linecount+2,t)/