import names
import random

desired_range = range(100)
people_names = {}
age = {}
money = {}
people = [people_names, age, money]

for i in desired_range:
    age[i] = random.randrange(11, 99)
    people_names[i] = names.get_first_name()
    money[i] = random.randrange(150, 13500)

rand_bot_index = random.randrange(1, 100)
print(
    f"Person {people_names[rand_bot_index]} is {age[rand_bot_index]} years old and has {money[rand_bot_index]} USD"
)
