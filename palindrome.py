#Author: Alex DiStasi
#File: palindrome.py
#Purpose: returns True if word is a palindrome and False if it is not

def checkPalindrome(inputString):
    backwardsStr =""
    #iterate through inputString backwards
    for i in range(len(inputString)-1,-1,-1):
        #create a reversed version of inputString
        backwardsStr+=(inputString[i]).lower()
    #iterate through inputString and compare to the reverse string. If an element has a different value, it is not a palindrome
    for i in range(0, len(inputString)):
        if inputString[i]!=backwardsStr[i]:
            return False
    return True

#Ask user for a word to check until user writes 'stop':
userWord = input("Enter a word to see if it is a palindrome. Type 'stop' to exit: ")
while (userWord.lower() != "stop"):
    print (checkPalindrome(userWord))
    userWord = input("Enter a word to see if it is a palindrome. Type 'stop' to exit: ")




