#leap year or not

def year(n):
    if (n%400 == 0 ) and (n%100 == 0):
        print(n,"is a leap year")

    elif (n%4 == 0) and (n%100 != 0):
        print(n,"is a leap year")

    else:
        print(n,"is a not leap year")
       

year(1800)          #output = 1800 is a not leap year