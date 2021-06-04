#Animal is a class ..
class Animal(object):
	pass
#dog ia-an Animal
class Dog(Animal):
	def __init__(self,name):
		#dog has-a name
		self.name = name

#cat is an Animal
class Cat(Animal):
	def __init__(self,name):
		#cat has-a name:
		self.name = name

#Person is a class
class Person(object):

	def __init__(self,name):
		#Person has-a name
		self.name = name
		#Person has-a pet
		self.pet = None

#Person is-a Employee
class Employee(Person):
	def __init__(self,name,salary):
		#Employee has-a name
		super(Employee,self).__init__(name)
		#Employee has-a salary
		self.salary = salary

#Fish is a class
class Fish(object):
	pass

#salmon is a fish
class Salmon(Fish):
	pass

#halibut is a fish
class Halibut(Fish):
	pass

rover = Dog('Rover')
satan = Cat('Satan')
mary = Person('mary')
mary.pet = 'satan'
frank = Employee('Frank',120000)
frank.pet = 'rover'
flipper = Fish()
crouse = Salmon()
harry = Halibut()

