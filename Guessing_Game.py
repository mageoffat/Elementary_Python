# Write a guessing game where the user has to guess a secret number.
#  After every guess the program tells the user whether their number was too large or too small.
#  At the end the number of tries needed should be printed.
#  It counts only as one try if they input the same number multiple times consecutively.

from random import randint
x = randint(0, 65536)
guess = -1
prev = 0
value = -1
tries = 0
while(x != value):
    guess = input("What is your guess?")
    try:
        value = int(guess)
    except:
        ValueError
    if (value == prev):
        print("you just guessed that number dummy")
    elif (value > x):
        tries += 1
        print("you guessed too high")
    elif (value < x):
        tries += 1
        print("you guessed too low")
    prev = value
print("You got it correct")
print(tries)
