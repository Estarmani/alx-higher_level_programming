#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = abs(number) % 10
stringmessage = "Last digit of {} is {}".format(number, LastDigit)
if number < 0:
    LastDigit = -(LastDigit)
if LastDigit > 5:
    print(f"{stringmessage} and is greater than 5")
elif LastDigit == 0:
    print(f"{stringmessage} and is 0")
elif LastDigit < 6:
    print(f"{stringmessage} and is less than 6 and not 0")
