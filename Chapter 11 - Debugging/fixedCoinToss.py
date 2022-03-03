# fixedCoinToss.py - Buggy coin toss program provided as an example

import random
import logging

# Normally I would have changed the config before commiting the program, however
# for the purpose of this task I will leave it as is
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)

guess = ""
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
    logging.debug(f"user input: {guess}")

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug(f"toss: {toss}")

if guess == "tails":
    guess = 0
else:
    guess = 1
logging.debug(f"guess: {guess}")

if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    while guess not in ("heads", "tails"):
        print("Enter heads or tails: ")
        guess = input()
        logging.debug(f"user input: {guess}")

    if guess == "tails":
        guess = 0
    else:
        guess = 1

    if toss == guess:
        print("You got it!")
        logging.debug(f"guess: {guess}")
        logging.debug(f"toss: {toss}")
    else:
        print("Nope. You are really bad at this game.")
        logging.debug(f"user input: {guess}")
        logging.debug(f"toss: {toss}")
