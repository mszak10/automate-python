# Chapter 6 - Manipulating Strings
# tablePrinter.py - Print list of lists of strings in a table
# TODO: Page 155 Points 2-4
# TODO: fix multiplayer support && win cond
# I can't do this today, I need to rest. Must figure out why points are funky and not saved properly
# TODO: fix point counting, I think they might be somehow shared between objects and I don't know why
# TODO: Make sure playerface is properly reset before each round
import random

green_dice = ['foot', 'foot', 'brain', 'brain', 'brain', 'gun']
yellow_dice = ['foot', 'foot', 'brain', 'brain', 'gun', 'gun']
red_dice = ['foot', 'foot', 'brain', 'gun', 'gun', 'gun']

diff_tab = ["Easy", "Normal", "Hard", "Extreme"]
# playerface = []
difficulty = 0
player_list = []

playercount = input("How many players?")


def set_difficulty(diff, add_yellow=404):  # Need to optimize this
    d = diff_tab[diff]
    dice_tab = []
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
        print(f'''Difficulty is {d}.
                    Following are how many dice there is:
                    Total: 13
                    Green: {green_num}
                    Yellow: {yellow_num}
                    Red: {red_num}
                    ''')
    else:
        for x in range(add_yellow):
            dice_tab.append("Y")

    return d, dice_tab


# Config:
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


class Game:
    def __init__(self, playernum=404):
        self.playernum = playernum

    playerface = []
    brainc = gunc = footc = points = 0
    once = True
    end = False
    eliminated = False

    def throw_dice(self, howmuch=3):
        # Take three dice and throw
        random_face = ""
        for z in range(howmuch):
            random_dice = random.choice(cup)
            if random_dice == "G":
                random_face = random.choice(green_dice)
            if random_dice == "Y":
                random_face = random.choice(yellow_dice)
            if random_dice == "R":
                random_face = random.choice(red_dice)
            list(cup).remove(random_dice)
            print(random_face, end=" ")
            self.playerface.append(random_face)
        print("")

    def round(self, player=404):
        self.throw_dice()
        self.gunc = self.brainc = self.footc = 0
        for i in self.playerface:
            if i == "gun":
                self.gunc += 1
            elif i == "brain":
                self.brainc += 1
            elif i == "foot":
                self.footc += 1
        self.playerface.clear()
        while True:
            reroll = input(f'''It's Player {player + 1}'s turn!
            You have:
            {self.points} points
            {self.brainc} brains
            {self.gunc} guns
            {self.footc} feet
            Would you like to reroll your {self.footc} foot dice and {3 - self.footc} new dice? (Y/N)''')
            if self.gunc > 2:
                print(f"Game over for Player {player + 1}!")
                self.eliminated = True
                break
            if reroll == "Y" and Game().end is not True:
                set_difficulty(difficulty, self.footc)
                self.footc = 0
                self.playerface.clear()
                self.throw_dice()
                for i in self.playerface:
                    if i == "gun":
                        self.gunc += 1
                    elif i == "brain":
                        self.brainc += 1
                    elif i == "foot":
                        self.footc += 1
                self.playerface.clear()
                if self.gunc > 2:
                    print(f"Game over for Player {player+1}!")
                    self.eliminated = True
                    self.playerface.clear()
                    break
                if self.brainc > 12 or self.points > 12:
                    print(f"Player {player+1} wins!")
                    Game().end = True
                    break
            elif reroll == "N":
                print("Round ended!")
                self.playerface.clear()
                break
            else:
                print("Input Y or N!")


for i in range(int(playercount)):
    player_list.append(Game(int(i)))

while True:  # NOTE: this goes into infinite loop when all players are eliminated before the game is ended
    i = 0
    # Place all the dice in the cup:
    cup = set_difficulty(difficulty)[1]
    for i in range(int(playercount)):
        if not player_list[i].eliminated:
            #if player_list[i].once:
             #   player_list[i].throw_dice()
            player_list[i].once = False
            player_list[i].round(i)
            if not player_list[i].eliminated:
                player_list[i].points = player_list[i].brainc
        else:
            print("Game Over!")
            Game(int(playercount)).end = True
            break
    if Game(int(playercount)).end:
        break

print("RESULTS:")
for i in range(int(playercount)):
    print(f"Player {i + 1}'s points: {player_list[i].points}")
