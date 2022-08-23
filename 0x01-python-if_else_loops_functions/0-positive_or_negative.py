#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = -10
while (i != number):
    i += 1
    print("the random value is :", number)
if (number > 0):
    print("is positive")
if (number == 0):
    print("is zero")
if (number < 0):
    print("is negative")
