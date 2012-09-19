# hw2objects.py objects/classes

class Meals(object):

	#__init__ automatically called when creating an objects
	def __init__(self, mealStr = None):   # i don't understand this part
		print "Logging new meal of the day:", mealStr
		self.meal = mealStr

	def set_meal(self, mealStr):
		self.meal = mealStr

meal1 = Meals("Breakfast")
meal1.set_meal("Yogurt")
meal1.time = 9

# print "This meal is:", type(meal1)
print "Breakfast: %s" % meal1.meal

print meal1.meal, "was eaten at", meal1.time, "AM."
