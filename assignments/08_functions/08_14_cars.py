'''
Logan Eyrich
Chapter 8
Difficulty: 5/10
'''

def make_car(manufacturer, model, **options):
	"""Return a dictionary with the car's information."""
	car = {'manufacturer': manufacturer, 'model': model}
	car.update(options)
	return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)