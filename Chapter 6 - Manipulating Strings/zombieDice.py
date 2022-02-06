# Chapter 6 - Manipulating Strings
# tablePrinter.py - Print list of lists of strings in a table
# TODO: Page 155 Points 2-4
# TODO: Properly counting how many guns and brains player has && multiplayer support && win cond
import random

green_dice = ['foot', 'foot', 'brain', 'brain', 'brain', 'gun']
yellow_dice = ['foot', 'foot', 'brain', 'brain', 'gun', 'gun']
red_dice = ['foot', 'foot', 'brain', 'gun', 'gun', 'gun']

diff_tab = ["Easy", "Normal", "Hard", "Extreme"]
random_face = ""
playerface = []
difficulty = gunc = brainc = footc = 0


def set_difficulty(diff):
    d = diff_tab[diff]
    if diff == 0:
        green_num = 7
        yellow_num = 4
        red_num = 2
    elif diff == 1:
        green_num = 5
        yellow_num = 3
        red_num = 5
    elif diff == 2:
        green_num = 4
        yellow_num = 3
        red_num = 6
    elif diff == 3:
        green_num = 3
        yellow_num = 3
        red_num = 7
    else:
        return 4, 0, 0, 0
    dice_tab = []
    for x in range(green_num):
        dice_tab.append("G")
    for x in range(yellow_num):
        dice_tab.append("Y")
    for x in range(red_num):
        dice_tab.append("R")

    print(f'''Difficulty is {d}.
            Following are how many dice there is:
            Total: 13
            Green: {green_num}
            Yellow: {yellow_num}
            Red: {red_num}
            ''')
    return d, dice_tab


def throw_dice(howmuch=3):
    # Take three dice and throw
    for i in range(howmuch):
        random_dice = random.choice(cup)
        if random_dice == "G":
            random_face = random.choice(green_dice)
        if random_dice == "Y":
            random_face = random.choice(yellow_dice)
        if random_dice == "R":
            random_face = random.choice(red_dice)
        list(cup).remove(random_dice)
        print(random_face, end=" ")
        playerface.append(random_face)
    print("")


# Config:
playercount = input("How many players?")  # Currently unused
while True:
    dd = False
    try:
        difficulty = int(input("Choose Difficulty (0-3)"))
        if not 0 <= difficulty > 3 and difficulty > -1:
            dd = True
    except ValueError:
        print("Error! Input correct value!")
    if dd:
        break

# Place all the dice in the cup:
cup = set_difficulty(difficulty)[1]

# Take three dice and throw (Default = 3)
throw_dice()

for i in playerface:
    if i == "gun":
        gunc += 1
    if i == "brain":
        brainc += 1
    if i == "foot":
        footc += 1

while True:
    reroll = input(f'''You have:
    {brainc} brains
    {gunc} guns
    {footc} feet
    Would you like to reroll your {footc} foot dice and {3-footc} new dice? (Y/N)''')
    if reroll == "Y":
        footc = 0
        throw_dice()
    elif reroll == "N":
        break
    else:
        print("Input Y or N!")
