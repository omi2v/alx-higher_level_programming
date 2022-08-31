#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    se = set(my_list)
    for num in se:
        sum += num
        return sum
