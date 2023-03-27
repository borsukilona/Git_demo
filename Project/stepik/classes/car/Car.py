class Car():

    def __init__(self, model, year, engine, price, milage):
        self.model = model
        self.year = year
        self.engine = engine
        self.price = price
        self.milage = milage
        self.wheel = 4

    def describe_car(self):
        description = f"New car is {self.model} of {self.year} year, " \
                      f"has {self.engine} engine capacity and has milage {self.milage} km. " \
                      f"The cost is {self.price}"
        print(description)


car = Car("Toyota", 2015, 1.6, 5000, 90000)
car.describe_car()
# New car is Toyota of 2015 year, has 1.6 engine capacity and has milage 90000 km. The cost is 5000


class Truck(Car):

    def __init__(self, model, year, engine, price, milage):
        super().__init__(model, year, engine, price, milage)
        self.wheel = 8


truck = Truck("MAZ", 1999, 2.5, 1000, 100000)
truck.describe_car()
# New car is MAZ of 1999 year, has 2.5 engine capacity and has milage 100000 km. The cost is 1000
