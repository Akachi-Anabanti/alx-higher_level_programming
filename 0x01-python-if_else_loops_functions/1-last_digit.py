#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# using modolus to get the last  digit of number
last_digit = abs(number) % 10
# apply sign
if number < 0:
    last_digit *= -1

if last_digit > 5:
    print(
            f"Last digit of {number} is "
            f"{last_digit} and is greater than 5"
        )
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(
            f"Last digit of {number} is "
            f"{last_digit} and is less than 6 and not 0"
        )
