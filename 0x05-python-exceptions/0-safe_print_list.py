#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while (i <= x - 1):
        try:
            item = my_list[i]
        except IndexError:
            print("")
            return i
        else:
            print(item, end="")
            i += 1
    print("")
    return i
