class MenuItem:
    """Models each menu Item"""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """Models the menu with drinks"""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=5, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_order(self):
        options = ""
        for option in self.menu:
            options += f"{option.name} - "
        return options

    def find_drink(self, order_name):
        for option in self.menu:
            if option.name == order_name:
                return option
        print("Sorry, item isn't available.")
