# Guess the number
# Chapter 3 - Functions
import random

guess = None
number = random.randint(1, 20)

print("Guess a number from 1 to 20 in 6 tries")
for guesses in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        break

if guess == number:
    print("Good job, you guessed " + str(number) + " correctly")
else:
    print("Sorry, the number was: " + str(number))
