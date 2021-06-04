'''
 it is simply extra documentation and has no impact 
 on how your classes work.
 class Name is a class of type object.
  class Name(object) is like saying 
  this is a basic simple class
  note: explicit is better than implicit
'''

class Other(object):

	def override(self):
		print('Other override()')

	def implicit(self):
		print('Other implicit()')

	def altered(self):
		print('Other altered()')



class Parent(object):

	def override(self):
		print('Parent override()')

	def implicit(self):
		print('Parent implicit()')

	def altered(self):
		print('Parent altered()')

class Child(object):

	def __init__(self):
		self.other = Other()

	def override(self):
		print('Child override()')

	def implicit(self):
		self.other.implicit()

	def altered(self):
		print('Child before Parent altered()')
		self.other.altered()
		print('Child after Parent/Other altered()')

'''
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
'''

son = Child()

son.implicit()
son.override()
son.altered()
