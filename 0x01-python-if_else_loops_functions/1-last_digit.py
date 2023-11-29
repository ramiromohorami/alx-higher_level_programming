#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    rest = number % 10
else:
    rest = (-1 * number) % 10  
if rest == 0:
    print(f"Last digit of {number} is {rest} and is 0")
elif rest > 5:
    print(f"Last digit of {number} is {rest} and is greater than 5")
else:
    print(f"Last digit of {number} is {rest} and is less than 6 and not 0")
