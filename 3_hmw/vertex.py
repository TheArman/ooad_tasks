import random


class Vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'


for _ in range(5):
    obj = Vertex(random.randint(-100, 100), random.randint(-100, 100))
    print(obj.__str__())
