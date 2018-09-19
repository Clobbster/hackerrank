# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# 9/14/18
import os

os.system('clear')
# 3
# 1, 2, 3,
# 4, 5, 6,
# 7, 8, 9

# list[0][0] == 1
# list[1][1] == 5
# list[2][2] == 9

# list[-0][-0] == 3
# list[-1][-1] == 5
# list[-2][-2] == 7

# I need i[0][0] + i[1][1] + i[2][2]

list1 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

input_var = 3
iv1       = 0
iv2       = 0
var1      = 0
var2      = 0
answer    = 0

# Iterate forward over the list-of-lists
for i in list1:
    var1 += list1[iv1][iv1]
    if iv1 < input_var:
        iv1 += 1

# Iterate backwards over the list-of-lists
for i in list1:
    var2 += list1[iv2][input_var - iv2 - 1]
    if iv2 < input_var:
        iv2 += 1

# Ensure the answer is a positive integer
if var1 > var2:
    answer = var1 - var2
elif var1 < var2:
    answer = var2 - var1

print(var1)
print(var2)
print(answer)
