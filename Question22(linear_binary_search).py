#implementation of Linear and Binary search

##Linear search

def linear_search(n,a,key):
    f = 0
    for i in range (n):
        if (a[i] == key):
            f = 1
            pos = i+1
            break
    if f == 1 :
        print("Number is on position no.",pos)
    else:
        print("number not found")

n = int(input("Enter length of the list: "))
a = []
for i in range(n):
    value = int(input("Enter values in list :"))
    a.append(value)

key = int(input("Enter number to search: "))

linear_search(n,a,key)

##Binary search

def binary_search(n,a,key):
    i =0
    j = n-1
    f = 0 
    while i < j and f == 0 :
        mid = (i+j)//2
        if a[mid] == key :
             f = 1                 
             pos  = mid+1
        if a[mid] > key :
            j = mid-1
        if a[mid] < key :
            j = mid+1

    if f == 1 :
        print("Number is at postion no.",pos)
    else:
        print("Number is not found")
    
n = int(input("Enter length of the list: "))
a = []                                                
for i in range(n):
    value = int(input("Enter values in list :")) 
    a.append(value)                             ##remember to keep the list sorted

key = int(input("Enter number to search: "))

binary_search(n,a,key)