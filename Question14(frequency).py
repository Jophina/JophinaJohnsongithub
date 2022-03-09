#program to find the frequency of each letter in a sentence
text = input("Enter a phrase :")
f = {}
for i in text:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
print("Frequency of each letter :", f)


