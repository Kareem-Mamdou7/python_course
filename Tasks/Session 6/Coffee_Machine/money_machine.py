class MoneyMachine:
    currency = "$"
    coin_value = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self):
        self.profit = 0
        self.money_recieved = 0

    def report(self):
        print(f"Money: {self.profit}{self.currency}")

    def process_coins(self):
        print("please insert Coins.")
        for coin in self.coin_value:
            self.money_recieved += (
                int(input(f"How Many {coin}?: ")) * self.coin_value[coin]
            )
        return self.money_recieved

    def make_payment(self, cost):
        self.process_coins()
        if self.money_recieved >= cost:
            change = round(self.money_recieved - cost, 2)
            print(f"Here's your change: {change}{self.currency} in change.")
            self.profit += cost
            self.money_recieved = 0
            return True

        else:
            print("Enter Enough money you broke monkey...\n")
            self.money_recieved = 0
            return False
