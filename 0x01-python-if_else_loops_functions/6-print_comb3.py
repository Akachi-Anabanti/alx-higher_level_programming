#!/usr/bin/python3

# print all possible different combinations of two digits.

for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", " if j < 9 else "\n")