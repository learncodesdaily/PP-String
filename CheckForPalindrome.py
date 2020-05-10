def checkPalidrome(str):
    if(str == str[::-1]):
        print("The String ",str," is a Palindrome")
    else:
        print("The String ", str, " is Not a Palindrome")
        
str = input("Enter an String : ")
checkPalidrome(str)