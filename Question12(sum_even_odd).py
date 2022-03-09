#(a)Sum of first n odd natural numbers

m = int(input("Enter the number: "))
sum=0
i=1
while(i<=m):
    sum=sum+i
    i=i+2
print("sum of odd numbers=",sum)


#(b) Sum of first n even natural numbers

n = int(input("Enter the number: "))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i=i+2
print("sum of even numbers=",sum)
