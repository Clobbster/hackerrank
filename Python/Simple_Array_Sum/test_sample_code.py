def simpleArraySum(n, *argv):
    #
    # Write your code here.
    list1 = []
    summed = 0
    
    for i in argv:
        list1.append(i)
    
    for j in list1:
        summed += j
    
    print(summed)
    print(list1)
simpleArraySum(6, 1, 2, 3, 4, 10, 11)