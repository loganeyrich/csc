'''
Logan Eyrich
Chapter 9
Difficulty: 4/10
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant("Python Cafe", "Italian")
print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Customers served: {restaurant.number_served}")