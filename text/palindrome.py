palindrome = input("What word or phrase would you like to check?")
palindromeNoSpace = palindrome.replace(" ","")
lengthCheck = False
wordLength = 0

while lengthCheck == False:
    if len(palindrome) == 0:
        print("Please enter a word or phrase")
        palindrome = input("What word or phrase would you like to check?")
        palindromeNoSpace = palindrome.replace(" ","")
    else:
        palindromeReversed = palindromeNoSpace[::-1]
        if palindromeNoSpace == palindromeReversed:
            print(palindrome + " is a Palindrome!")
            lengthCheck = True
        else:
            print(palindrome + " is not a Palindrome")
            palindrome = input("What word or phrase would you like to check?")
            palindromeNoSpace = palindrome.replace(" ","")
            lengthCheck = False
    