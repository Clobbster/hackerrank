# Write a function that determines if a given input year is a leap year.

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
        
    
    print(leap)

is_leap(1900)
