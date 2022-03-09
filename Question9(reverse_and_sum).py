def rev(i):
    rev=0
    while(i>0):
      rev=(rev*10)+i%10
      i=i//10
    print("reverse=",rev)



def sum(i) :
    sum=0
    while(i>0):
      sum=sum+i%10
      i=i//10
    print("sum of digits=",sum)


rev(25)
sum(25)
#output
# reverse= 52
# sum of digits= 7
