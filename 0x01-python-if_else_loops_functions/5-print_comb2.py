#!/usr/bin/python3

# print number in ascending order from 0 to 99

for number in range(100):
    if number == 99:
        print(number)
    else:
        print("{:02d}".format(number), end=", ")
