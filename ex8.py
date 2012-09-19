# when changing out the first two %r with %s, 
#the print excludes the single quotes for the %s variables
formatter = "%s %s %r %r"

print formatter % (1, 2, 3, 4)
# python will print out the one two, etc with single quotes
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter,formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)