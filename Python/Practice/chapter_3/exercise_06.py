from random import randint

wn = randint(1, 100)

guess = 0
game_over = True
userinput = int(input("Guess a number : "))

while game_over:
    if userinput==wn:
        print(f"YOU WIN !!!\nYou guessed in {guess} times \U0001F60A")
        game_over = False
    else:
        if userinput<wn:
            print("too loow")
        else: 
            print("too high")
        userinput = int(input("Guess again : "))
        guess += 1
