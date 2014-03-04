from ex45class import *


PrintClass()

class Animal(Person):
	def __init__(self,name,sex):
		super(Animal,self).__init__(name,sex)
		
	
	
animal  = Animal("xiaoqiang","man")

print  animal.getAll()

class Dog(object):
	def __init__(self):
		self.dog = Person("wangcai","girl")
	
	def getNameAndSex(self):
		return self.dog.getAll()
		
dog = Dog()
print dog.getNameAndSex()