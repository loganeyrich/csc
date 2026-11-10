'''
Logan Eyrich
Chapter 9
Difficulty: 5/10
'''

class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

    def describe_stand(self):
        print(f"We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand(["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"])
stand.describe_stand()
