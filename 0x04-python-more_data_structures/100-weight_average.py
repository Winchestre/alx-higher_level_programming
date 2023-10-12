#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    add_score = 0
    add_weight = 0
    for _tuple in my_list:
        add_score += _tuple[0] * _tuple[1]
        add_weight += _tuple[1]
    return add_score / add_weight
