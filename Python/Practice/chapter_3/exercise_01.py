# EXERCISE : NUMBER GUISSING GAME

# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.

# if user didn't guessed correctly then : 
# 	if user guessed lower than actual number then print "too low"
# 	if user guessed higher than actual number then print "too high"

# google "how to generate random number in python" to generate random wining_number

from random import randint

winning_number = randint(1,100)

user_guess = int(input("Guess a number b/t 1 and 100 : "))

if user_guess < winning_number:
    print("too low")
else: 
    print("too high")

print(f"winning number is : {winning_number}")