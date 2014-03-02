stuff = ['Test','This','OUT']
print stuff
print ''.join(stuff)
print ' '.join(stuff)
print '  '.join(stuff)
print 'a'.join(stuff)


class TheThing(object):
	def __init__(self):
		self.number = 0
	def some_function(self):
		print "I got called."
	def add_me_up(self,more):
		self.number += more
		return self.number
		
a = TheThing()
b = TheThing()
print a.number
print b.number
c = a.add_me_up(10)
print c




class TheMultiplier(object):
	def __init__(self,base):
		self.base = base
	def do_it(self,m):
		return m*self.base
		
x = TheMultiplier(a.number)
print x.do_it(b.number)



