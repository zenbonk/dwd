#variable x equals what's in the "" and the %d shows on the print line 
#as the value on the right of th string, which is preceded by a modulus % sign
x = "There are %d types of people." % 10
# binary is a variable for "binary"
binary = "binary"
# do_not is a variable for "don't", which will be what's printed when commanded
do_not = "don't"
# y will print out the phrase in "" and replace from left to right the %s
# with the value variables after the % modulus sign that comes after the "", in ()
y = "Those who know %s and those who %s." % (binary, do_not)

#will print out "There are 10 types of peolple"
print x
# will print out "Those who know binary and those who don't"
print y

# %r somehow tests/debugs and prints all for the value x, which is "There are 10..."
print "I said: %r." % x
# prints the variable y to users. why %s is used, slight variation from %r
print "I also said: '%s'." % y

# variable hilarious is False
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"
# will print "Isn't that joke so funny?! False" False is the value % hilarious attributed to it
print joke_evaluation % hilarious
# using + to add w and e makes a longer string because it attaches the two together (in order left-right)
w = "This is the left side of..."
e = "a string with a right side."

print w + e