# a program that tells a user that you guessed too high or low
# Author: James Connolly

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))

    print("Well done!Yes the number", numberToGuess)




