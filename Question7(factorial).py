#factorial using while loop

i=int(input("Enter number:"))
fac=1

if (i<0):
    print("Please enter a positive number")

elif (i == 0):
    print("Factorial = 1" )

else:
    while(i>0):
        fac=fac*i
        i=i-1
print("Factorial=",fac)

#factorial using for loop

m=int(input("Enter number:"))
fac=1

if (m == 0):
    print("Factorial = 1" )

else:
    for x in range(1,m+1):
        fac = fac*x
        x = x+1
print("Factorial=",fac)
    
#factorial using recurssion

def factorial(n) :
    if n == 0 or n == 1:
         return 1                              
    else:
        return n * factorial(n-1)

print(factorial(5))   #output = 120