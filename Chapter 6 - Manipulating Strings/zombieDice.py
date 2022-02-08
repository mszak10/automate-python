# Chapter 6 - Manipulating Strings
# tablePrinter.py - Print list of lists of strings in a table
# TODO: Page 155 Points 3-4
# TODO: Re-rolling your own dice properly instead of returning it into the cup
# TODO: Tiebreaks
# TODO: add condition where all 13 dice have been thrown
import os
import random
import time

# Current version:
VERSION = "beta 1.1.1"

diff_tab = ["Easy", "Normal", "Hard", "Extreme"]
# playerface = []
difficulty = playercount = 0
player_list = []
end = once = None
results = [0, 0]

print(f"Welcome to the Zombie Dice game (Version {VERSION})")

while True:  # How many players (max 20)
    out = False
    try:
        playercount = int(input("How many players? "))
        if playercount > -1 and 1 <= playercount < 20:
            out = True
    except ValueError:
        print("Input correct value! (between 1 and 20)")
    if out:
        break


def clear():
    os.system('cls')


def set_difficulty(diff, add_yellow=404):  # Need to optimize this
    d = diff_tab[diff]  # This function sets the dice in the cup
    dice_tab = []  # according to the difficulty chosen by the user
    dice_tab.clear()
    global once
    if once is None:  # this makes sure difficulty info is printed only once
        once = True
    if add_yellow == 404:
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
        for x in range(green_num):
            dice_tab.append("G")
        for x in range(yellow_num):
            dice_tab.append("Y")
        for x in range(red_num):
            dice_tab.append("R")
        if once:
            print(f'''Difficulty is {d}.
                                Following are how many dice there is:
                                Total: 13
                                Green: {green_num}
                                Yellow: {yellow_num}
                                Red: {red_num}
                                ''')
            time.sleep(2)
            once = False
    else:
        for x in range(add_yellow):
            dice_tab.append("Y")

    return d, dice_tab


# Config:
while True:  # Vaidation of user input
    dd = False
    try:
        difficulty = int(input("Choose Difficulty (0-3) "))
        if not 0 <= difficulty > 3 and difficulty > -1:
            dd = True
    except ValueError:
        print("Error! Input correct value!")
    if dd:
        break


class Game:
    def __init__(self, playernum=404):
        self.playernum = playernum  # Number of players

    green_dice = ['foot', 'foot', 'brain', 'brain', 'brain', 'gun']
    yellow_dice = ['foot', 'foot', 'brain', 'brain', 'gun', 'gun']
    red_dice = ['foot', 'foot', 'brain', 'gun', 'gun', 'gun']
    playerface = []
    brainc = gunc = footc = points = 0
    eliminated = False
    global end  # if end is True, the game will end after round is finished
    if end is None:
        end = False

    def throw_dice(self, howmuch=3):
        # Take three dice from the cup and throw
        random_face = ""
        foot_dice = ["", "", ""]
        r_dice = []
        r_dice.clear()
        print("You rolled:".center(21, "="))
        for z in range(howmuch):
            random_dice = random.choice(cup)
            if random_dice == "G":
                random_face = random.choice(self.green_dice)
            if random_dice == "Y":
                random_face = random.choice(self.yellow_dice)
            if random_dice == "R":
                random_face = random.choice(self.red_dice)
            if random_face == "foot":
                foot_dice[z] = random_dice
            r_dice.append(random_dice)
            list(cup).remove(random_dice)  # Does not remove dice from cup (possibly has no access to cup var)
            print(random_face.center(7, "."), end="")
            self.playerface.append(random_face)
        print("")
        print("Dice colors:".center(21, "="))
        for y in range(howmuch):
            print(r_dice[y].center(7, "."), end="")
        print("")
        print("Dice in cup:".center(21, "="))
        print(list(cup))
        print("")

    def round(self, player=404):
        global end
        self.throw_dice()
        self.gunc = self.brainc = self.footc = 0
        for x in self.playerface:  # set variables that will be worked on (only active during one player's round)
            if x == "gun":
                self.gunc += 1
            elif x == "brain":
                self.brainc += 1
            elif x == "foot":
                self.footc += 1
        self.playerface.clear()
        while True:
            if self.brainc > 12 or self.points > 12:  # if player exceeds 12 points/brains - he wins
                self.points += self.brainc
                print(f"Player {player + 1} wins!")
                end = True
                break
            if self.gunc > 2:  # if player rolled 3+ guns, he looses
                print(f"Game over for Player {player + 1}!")
                self.eliminated = True
                time.sleep(3)
                break
            print(f"It's Player {player + 1}'s turn!")
            print("You have:".center(21, "."))
            print(f"{self.points}".rjust(7, ".") + " points".ljust(14, "."))
            print(f"{self.brainc}".rjust(7, ".") + " brains".ljust(14, "."))
            print(f"{self.gunc}".rjust(7, ".") + " guns".ljust(14, "."))
            print(f"{self.footc}".rjust(7, ".") + " feet".ljust(14, "."))
            reroll = input(f"Would you like to reroll your {self.footc} foot dice and {3 - self.footc} new dice? (Y/N)")
            if reroll == "Y" and end is not True:  # if player rerolls
                set_difficulty(difficulty, self.footc)  # add the footdice to the cup (as yellow dice)
                self.footc = 0
                self.playerface.clear()
                clear()
                self.throw_dice()
                for x in self.playerface:
                    if x == "gun":
                        self.gunc += 1
                    elif x == "brain":
                        self.brainc += 1
                    elif x == "foot":
                        self.footc += 1
                self.playerface.clear()
                if self.gunc > 2:
                    print(f"Game over for Player {player + 1}!")
                    self.eliminated = True
                    self.playerface.clear()
                    time.sleep(3)
                    clear()
                    break
                if self.brainc > 12 or self.points > 12:
                    self.points += self.brainc
                    print(f"Player {player + 1} wins!")
                    end = True
                    break
            elif reroll == "N" and end is not True:  # if player doesn't reroll, he gets a point for each brain
                print("Round ended!")
                self.points += self.brainc
                self.playerface.clear()
                clear()
                if self.brainc > 12 or self.points > 12:
                    print(f"Player {player + 1} wins!")
                    end = True
                    break
                break
            elif end:
                break
            else:
                print("Input Y or N!")
                time.sleep(2)
                clear()


for i in range(int(playercount)):  # add {playercount} objects of class Game (players)
    player_list.append(Game(int(i)))

while True:
    # Place all the dice in the cup:
    # player_list[i] = player object number i + 1 (list of objects of class Game)
    cup = set_difficulty(difficulty)[1]
    for i in range(int(playercount)):
        clear()
        if not player_list[i].eliminated:
            player_list[i].round(i)
        else:
            print(f"Skipping Player {i + 1}")
            time.sleep(.5)
            continue
    if end:
        break
    for i in range(int(playercount)):  # checks if all players are eliminated - if not the game goes on
        end = True
        if not player_list[i].eliminated:
            end = False
            break
    if end:
        break

clear()
print("RESULTS".center(21, "="))
for i in range(int(playercount)):
    print(f"Player {i + 1}'s points: {player_list[i].points}")
    if player_list[i].points > results[1]:
        results[1] = player_list[i].points
        results[0] = i
print(f"\nPlayer {results[0] + 1} won with {results[1]} points!")
