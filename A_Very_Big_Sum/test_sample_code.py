# put stuff here
list_to_sum = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def sum_func(a):

    summed_number = 0

    for i in a:
        summed_number += i

    return summed_number

holder = sum_func(list_to_sum)
print(holder)