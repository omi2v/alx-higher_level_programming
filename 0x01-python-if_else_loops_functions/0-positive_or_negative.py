#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = -10
while (i != number):
    i += 1
if (number > 0):
    print(number, "is positive")
if (number == 0):
    print(number, "is zero")
if (number < 0):
    print(number, "is negative")
