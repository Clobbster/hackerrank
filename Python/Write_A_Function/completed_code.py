# Sample code worked as is and didn't need further adjustments to work within hackerrank

def is_leap(year):
    leap = ""
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
        
    return leap


