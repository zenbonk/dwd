# making function with arguments inside () with : afterward
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# indent 4 spaces
	#the %d will always print the new cheese_count and new boxes_of_crackers
	    print "You have %d cheeses!" % cheese_count
	    print "You have %d boxes of crackers!" % boxes_of_crackers
	    print "Man that's enough for a party!"
	    print "Get a blanket.\n"

# eventually calling this function with new line, 4 times.
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calling function and using variables instead of args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calling function cheese_and_crackers to add up for new variables 
# amount_of_cheese then amount_of_crackers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calling function cheese_and_crackers, with math adding variables 
# with hard numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
