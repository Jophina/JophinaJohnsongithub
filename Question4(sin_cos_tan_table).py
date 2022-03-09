print("Table of sine,cosine and tangent in the range(0,10) with increment of 0.2")

import math

def sinx():
    for x in range(0,11,) :
        print(math.sin(x))
        x = x+0.2

def cosx():
    for x in range(0,11,) :
        print(math.cos(x))
        x = x+0.2

def tanx():
    for x in range(0,11,) :
        print(math.cos(x))
        x = x+0.2
print("Table for sine")
sinx()
print("Table for cosine")
cosx() 
print("Table for tan")
tanx()