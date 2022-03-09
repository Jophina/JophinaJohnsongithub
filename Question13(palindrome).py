#program to chcek if a string is palindrome or not

def palindrome(s):
    if(s == s[::-1]):                        #the reverse remains same as input(palindrome)
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

palindrome("truiurt")

#output = The string is palindrome