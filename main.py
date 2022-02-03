# file for currently worked on code (if unfinished)
# Next Chapter: 5 (Dictionaries and Structuring Data)
# TicTacToe without win condition - to be finished
tb = {
    'tL': ' ', 'tM': ' ', 'tR': ' ',
    'mL': ' ', 'mM': ' ', 'mR': ' ',
    'bL': ' ', 'bM': ' ', 'bR': ' '
}


def printboard():
    print(tb['tL'] + " | " + tb['tM'] + " | " + tb['tR'] + " | ")
    print("--+---+---+")
    print(tb['mL'] + " | " + tb['mM'] + " | " + tb['mR'] + " | ")
    print("--+---+---+")
    print(tb['bL'] + " | " + tb['bM'] + " | " + tb['bR'] + " | ")
    print("--+---+---+")


BinO = bin(0)
binX = bin(0)
move = ' '
turn = 'X'
print("Welcome to TicTacToe! Possible moves are:\ntL tM tR\nmL mM mR\nbL bM bR")
for i in range(9):
    printboard()
    print("It's player's " + turn + " turn. Where to set your " + turn + "?")
    while True:
        try:
            move = str(input())
            if tb[move] == ' ':
                break
            else:
                print("This spot is already taken by the other player!")
        except KeyError:
            print("Incorrect move!")
    tb[move] = turn
    tblist = list(tb.values())

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard()
