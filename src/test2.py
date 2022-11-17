import names
import random

bots_list = []


class Bot:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def say_hello(self):
        print(f"hello! my name is {self.name}")

    def __str__(self):
        return self.get_info()

    def get_info(self):
        return f"{self.name} is {self.age} years old, and has {self.money} US Dollars."

    @classmethod
    def create_random(cls):
        rand_name = names.get_first_name()
        rand_age = random.randrange(11, 99)
        rand_money = random.randrange(150, 13500)
        b = cls(rand_name, rand_age, rand_money)
        return b


# b1 = Bot("max", 25, 1000)
b1 = Bot.create_random()
b1.say_hello()

for i in range(5):
    bots_list.append(Bot.create_random())


for b in bots_list:
    print(b.get_info())
