class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        print(f"Water: {self.resources["water"]}ml")
        print(f"milk: {self.resources["milk"]}ml")
        print(f"Coffee: {self.resources["coffee"]}ml")

    def is_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, There's no enough {item}")
                can_make = False
            return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here's your {order.name}, Enjoy!")
