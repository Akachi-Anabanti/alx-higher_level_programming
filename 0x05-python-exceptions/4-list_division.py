#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        try:
            qt = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            qt = 0
            print("division by 0")
        except (TypeError, ValueError):
            qt = 0
            print("wrong type")
        except IndexError:
            print("out of range")
        result.append(qt)
    return result
