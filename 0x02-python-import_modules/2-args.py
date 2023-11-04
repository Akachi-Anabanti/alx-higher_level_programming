#!/usr/bin/python3

# A program that prints the number of adn list of its
# arguments

# import modules
import sys


def print_args():
    args = sys.argv

    if len(args) == 1:
        print('0 arguments.')
    elif len(args) == 2:
        print('1 argument:')
        print('1: {}'.format(args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))

        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    print_args()
