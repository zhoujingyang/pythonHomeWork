#_*_coding:utf-8_*_

people = 30
cars = 40
buses = 15
if cars > people:#如果cars > people将打印
	print "We should take the cars."
elif cars < people:# 否则如果cars < people将打印
	print "We should not take the cars."
else:#否则将打印
	print "We can't decide."
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."