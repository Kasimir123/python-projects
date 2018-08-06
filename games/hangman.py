import re
print ("Welcome to Hangman, please enter a word which you would like to use for the game, and then enter how many failed guesses you wish to give to the players.")

# Initializes constants for the program
word = input("What is the word?")

# Checks to see if the player actually put a word or phrase into the input
if len(word) <= 0:
	print ("Please write a word or phrase")
	while len(word) <= 0:
		word = input("What is the word?")
		
# Storage for all the letters that were already guessed
guesses = []
# The number of incorrect guesses that the players will get
counter = input("How many missed guesses do you want to give the players?")

# Makes sure the user inputs a reasonable number of incorrect guesses
if counter <= 0 or counter >= 10:
	print ("Number of guesses must be greater than 0 and less than 10")
	while counter <= 0:
		counter = input("How many missed guesses do you want to give the players?")
		
# Shows what letters have been revealed and which ones still need to be guessed
reveal = []

# creates a space between the original questions and the game - i = the number of spaces wanted
i = 30
for each in word:
	reveal.append("_")
while i > 0:
	print ("|")
	i -= 1
	
# Checks if there are spaces in the phrase, if yes, then it replaces the empty spaces with a space 
if " " in word:
	for m in re.finditer(" ", word):
		m = m.start()
		reveal[m] = " "
		
print (reveal)

# The loop will not start again if there are no incorrect guesses left
while counter > 0:
#  If there have been previous guesses then this if loop will print them
	if len(guesses) != 0:
		print ("Guesses so far: ")
		print (guesses)
# Asks the player for their next guess 
	guess = input("What is your guess?")
# Checks if the guess is only 1 letter, if the letter has been guessed before, if the user wishes to quit the game
	if len(guess) == 1 :
		if guess not in guesses:
			guesses.append(guess)
# This if statement and for loop find if the letter is in the word or phrase and replace the spaces in reveal with the correct letter based on their position
			if guess in word:
				for m in re.finditer(guess, word):
					m = m.start()
					reveal[m] = guess
			else:
				print ("You have guessed incorrectly")
				counter = counter - 1
		else:
			print ("You have already used this letter")
	elif guess == "quit":
		break
	else:
		print ("Your guess is longer than 1 letter")
# Shows the incorrect guesses left and leters revealed
	print (reveal)
	print ("Incorrect guesses left:")
	print (counter)
# Checks if the player has won or lost
	if "_" not in reveal:
		print ("Congrats, you have won")
		break 
	elif counter == 0:
		print ("You have lost")
		break
