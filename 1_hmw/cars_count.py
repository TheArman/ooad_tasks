class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # self.count_cars()
        Car.count_cars_with_classmethod()
        self.__str__()

    def __str__(self):
        return f'{self.make}, {self.model}, {self.year}'

    # def count_cars(self):
    #     Car.total_cars += 1
    #     return Car.total_cars - 1

    @classmethod
    def count_cars_with_classmethod(cls):
        cls.total_cars += 1
        return cls.total_cars


p1 = Car('mazda', 6, 2012)
p2 = Car('bmw', 'm6', 2012)
p3 = Car('bmw', 'x6', 2012)
p4 = Car('mercedes', 'cls', 2012)
print(p1)
print(p2)
print(p3)
print(p4)
# print(f'counts of cars: {p1.count_cars().}')
print(f'counts of cars: {Car.total_cars}.')
