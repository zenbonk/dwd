# i is a variable for the number 0
i = 0
# this is a list [] of numbers variable
numbers = []

#starting new block of code with :
# while list number i is less than 6 add (append) i to old i
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

# in this while loop, i will be i+=1 until it hits 6
	i = i + 1
	print "Numbers now: ", numbers

# will print numbers now, what ever new i list value i is
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num