import random
import pyinputplus as pyip
points = 0

print("Welcome to multiplication quiz!")
for i in range(10):
    first_num = random.randint(0, 9)
    second_num = random.randint(0, 9)
    answer = first_num * second_num
    guess = pyip.inputInt(prompt=f"Multiply {first_num} * {second_num}:", min=0, max=100)
    if guess == answer:
        print("Correct!")
        points += 1
    else:
        print(f"Incorrect! You answered {guess} and the answer is {answer}")

print(f"Your points are {points}/10")
