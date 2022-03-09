#dictionary where keys are numbers and values are cubes of the numbers
n = int(input("Enter a number:"))
d = dict()
for i in range(1, n+1):
    d[i] = i ** 3
print("The dictionary of cubes upto given number = ", d)
