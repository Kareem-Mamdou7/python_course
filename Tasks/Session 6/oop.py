class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.__speed = 0  # Private attribute

    def accelerate(self):
        self.__speed = 5
        print(self.__speed)


my_car = Car("Tesla", "X", "2023", "Black")
my_car.accelerate()
