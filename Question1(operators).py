#Arithmatic operators

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
add = a+b
sub = a-b
mul = a*b
div = a/b
di  = a//b
rim = a%b
pow = a**b
print("adittion=",add)
print("subtraction=",sub)
print("multiplication=",mul)
print("float division=",div)
print("integer division=",di)
print("when dividing",a, "by", b,"remainder = ",rim)
print(a,"to the power",b,"=",pow)

#Relational Operators

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

print(x, "> ",y , "is",x > y)        #greater than(>)
print(x, "< ",y , "is",x < y)        #less than(<)
print(x, "==" ,y, "is",x == y)      #Equals to (==)
print(x, "!=" ,y, "is",x != y)      #not equals to(!=)
print(x, ">=" ,y, "is",x >= y)      #greater than eqaul to(>=)
print(x, "<=" ,y, "is",x <= y)      #less than eqaul to(<=)

#Logical Operators

s = True
r = False

print("s and r", s and r)
print("s or r", s or r)
print("not r", not r)

#Bitwise Operators

m = int(input("Enter first number:"))
n = int(input("Enter second number:"))

print(m,"&",n,"is = ", m&n)   #Bitwise and operation
print(m,"|",n,"is = ", m|n)   #Bitwise or operation
print(m,"^",n,"is = ", m^n)   #Bitwise xor operation
print("~",n,"is = ", ~n)      #Bitwise not operation
print(m,"<<",n,"is = ", m<<n) #left shift operation
print(m,">>",n,"is = ", m>>n) #right shift operation