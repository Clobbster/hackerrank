# Write a function that prints consequtive numbers from 1 to N for N without using string meathods.

def printFunc(N):

    print(*range(1, N + 1), sep="")

printFunc(50)
