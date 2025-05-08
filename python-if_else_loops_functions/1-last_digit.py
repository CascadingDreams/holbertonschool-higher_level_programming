#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_number = number % 10
else:
    last_number = -(abs(number) % 10)

message = "Last digit of {} is {}".format(number, last_number)
if last_number > 5:
    message += " and is greater than 5"
elif last_number == 0:
    message += " and is 0"
else:
    message += " and is less than 6 and not 0"
print(message)
