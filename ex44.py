class Parent(object):
	def implicit(self):
		print "PARENT implicit"
	def override(self):
		print "PARENT override()"
	def altered(self):
		print "PARENT altered"
class Child (Parent):
	def override(self):
		print "CHILD override"
	def altered(self):
		print "CHILD,before parent altered()"
		super(Child,self).altered()
		print "child,after parent altered()"
	
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.override()
son.override()
dad.altered()
son.altered()

class Other(object):
	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"

class Child_one(object):
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "CHILD_one override()"
	
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son_one = Child_one()
son_one.implicit()
son_one.override()
son_one.altered()









