name = 'Zed A. Shaw'
age = 35 # not a lie

# extra credit 4
# 1cm = 0.3937in 1in = 2.54cm

# to get centimeters multiply inches by 2.54

# to get inches divide centimeters by 2.54

#1lb /

height_inches = 74 # inches
height_cm = 74 * 2.54 #cm
weight = 180 # lbs
weight_kg = weight/2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print "I weigh %s pounds" %(weight)
print "I weigh %s kilos" %(weight_kg)

print "He's %d cm tall." %height_cm
print "Let's talk about %s." % name
print "He's %d inches tall." % height_inches
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_inches, weight, age + height_inches + weight)