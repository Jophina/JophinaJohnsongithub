#Least common multiple of two numbers

def lcm(a,b):
    if a >b :
        greater = a
    else: 
        greater = b

    while (True):
        if((greater%a == 0) and (greater%b == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

print(lcm(25,45)) 

#output = 225