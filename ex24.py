print "Let's practice everything."
print "you\'d need to know \'about escapes whit \\ that do \n new lines \t tabs."

poem = """
\tthe lovely world
with logic so firmly plated
con not discern \nthe needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\t where there is none
"""

print "-----------------"
print poem 
print "-----------------"

five = 10-2+3-6
print "this should be five : %s " % five

def secret_formula (started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "whit a starting point of : %d" % start_point
print "we would have %d beans,%d jars,and %d crates." % (beans,jars,crates)

start_point  = start_point / 10

print "we can also do that this way:"
print "we would have %d beans, %d jars, and %d crates." % secret_formula(start_point)



