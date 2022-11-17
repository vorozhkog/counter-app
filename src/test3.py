import names
import random


class Bot:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money


for i in range(5):
    Bot(names.get_first_name(), random.randrange(11, 99), random.randrange(150, 13500))
