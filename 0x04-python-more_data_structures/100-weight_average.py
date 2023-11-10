#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    tup = ((A1,B1), (A2, B2))
    weighted_average = sum(Ai x Bi) / sum(Bi) from i = 0 to i = i
    """
    total_prod = sum([x * y for x, y in my_list])
    total_weight = sum([item[1] for item in my_list])
    return total_prod / total_weight
