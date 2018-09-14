#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob   = 0
    
    function_array = []
    
    for item1, item2 in zip(a, b):
        if item1 > item2:
            alice += 1
        elif item1 < item2:
            bob += 1
        else:
            pass
    
    function_array = [alice, bob]
    return function_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

