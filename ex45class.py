def PrintClass():
	print "the class is printing"
	
class Person(object):
	def __init__(self,name,sex):
		self.name = name 
		self.sex = sex
		
	def getAll(self):
		return self.name,self.sex
		