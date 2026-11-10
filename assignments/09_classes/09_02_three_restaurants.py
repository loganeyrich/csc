'''
Logan Eyrich
Chapter 9
Difficulty: 2/10
'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

python_cafe = Restaurant("Python Cafe", "Italian")
sunrise_diner = Restaurant("Sunrise Diner", "American")
sakura_sushi = Restaurant("Sakura Sushi", "Japanese")

python_cafe.describe_restaurant()
sunrise_diner.describe_restaurant()
sakura_sushi.describe_restaurant()
