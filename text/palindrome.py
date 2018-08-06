palindrome = input("What word or phrase would you like to check?")
lengthCheck = False
wordLength = 0

while lengthCheck == False:
    if len(palindrome) == 0:
        print("Please enter a word or phrase")
        palindrome = input("What word or phrase would you like to check?")
    else:
        palindromeReversed = palindrome[::-1]
        if palindrome == palindromeReversed:
            print(palindrome + " is a Palindrome!")
            lengthCheck = True
        else:
            print(palindrome + " is not a Palindrome")
            palindrome = input("What word or phrase would you like to check?")
            lengthCheck = False
    