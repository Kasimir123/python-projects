import re
print ("Welcome to Hangman, please enter a word which you would like to use for the game, and then enter how many failed guesses you wish to give to the players.")
word = input("What is the word?")
guesses = []
counter = int(input("How many missed guesses do you want to give the players?"))
reveal = []
i = 30
for each in word:
	reveal.append("_")
while i > 0:
	print ("|")
	i -= 1
print (reveal)
while counter > 0:
	if len(guesses) != 0:
		print ("Guesses so far: ")
		print (guesses)
	guess = input("What is your guess?")
	if len(guess) == 1 :
		if guess not in guesses:
			guesses.append(guess)
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
	print (reveal)
	print ("Incorrect guesses left:")
	print (counter)
	if "_" not in reveal:
		print ("Congrats, you have won")
		break 
	elif counter == 0:
		print ("You have lost")
		break
