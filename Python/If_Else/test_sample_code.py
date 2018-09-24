# For a input variable, write if/then ladder for the following:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

N = int(input("Please enter a number: "))

if N % 2 != 0:
    print("Weird")
elif N % 2 == 0:
    if (N >= 2) & (N <= 5):
        print("Not Weird")
    elif (N >= 6) & (N <= 20):
        print("Here")
        print("Weird")
    else:
        print("Not Weird")