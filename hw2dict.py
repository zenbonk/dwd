# dictionary
myMeals = {
	
	'Breakfast' : 'Granola',
	'Lunch' : 'Turkey Sandwich',
	'Snack' : 'Raisins',
	'Dinner' : 'Chicken Soup',
	
}
print 
print myMeals['Snack'], "are my favorite kind of snack... or they were just what was around."

print 
myMeals['Breakfast II'] = 'Yogurt'  # adding another meal
myMeals['Lunch II'] = 'Not Enough'
just_the_meal_type = myMeals.keys()  # list of meal type

just_the_foods = myMeals.values() # a list of foods

print len(myMeals), " meals eaten the last two days." # print number of meals total
print
print just_the_meal_type, "are the types of meals I had."
print just_the_foods, "are the kinds of foods I ate."
print
print dict(myMeals)

for m in myMeals:
	print m
	print m.get('Dinner'), 'was not', m.get('Dinner'), '!'
	print m.get('Breakfast II'), 'was', m.get('Lunch II')
