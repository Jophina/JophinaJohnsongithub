#performing functions on a list

def string():
    choice =int(input('''Enter your choice 
1 = length of the string
2 = maximum of three strrings
3 = Replace every successive character with #
4 = number of words in the string
'''))

    if choice == 1:
        n = input("Enter a string : ")
        l=len(n)
        print("The length of the string is =",l)      
    elif choice == 2:
        n1 = input("Enter 1st string : ")
        n2 = input("Enter 2nd string : ")
        n3 = input("Enter 3rd string : ")
        print("The maximum of the three strings is =",max(n1,n2,n3))    
    elif choice == 3:
        n = input("Enter a string : ")
        s = ""
        m = list(n)
        for i in range(len(n)):
            if (i%2 != 0):
                if m[i] == " ":
                    m[i] = " "
                else:
                    m[i] = "#"
        for x in m:
            s=s+x
        print("The sucessive character in the string is replaced with # :",s) 
    elif choice == 4:
            n = input("Enter a string : ")
            c = 0
            for y in n :
                if y == " " :
                    c += 1
            w = c+1
            print("The number of words = ",w) 
    else :
        print("Please Choose from the given option only")

string()