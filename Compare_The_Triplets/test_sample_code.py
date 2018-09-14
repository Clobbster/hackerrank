# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# 9/14/18

import os

os.system("clear")

list1, list2 = [5, 6, 7, 7], [3, 6, 10, 2]


def tripletfunc(a, b):
    completed_array = []
    alice = 0
    bob   = 0

    for item1, item2 in zip(a, b):
        if item1 > item2:
            alice += 1
        elif item1 < item2:
            bob += 1
        else:
            pass

    completed_array = [alice, bob]
    print(completed_array)

tripletfunc(list1,list2)