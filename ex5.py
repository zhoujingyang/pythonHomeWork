my_name = 'zed a.shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "Hs's %d pounds heavy." % my_weight
print "Actually that's not too heavy" 
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are ususlly %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)