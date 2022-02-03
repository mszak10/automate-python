# TicTacToe with win condition - not the best but works
tb = {
    'tL': ' ', 'tM': ' ', 'tR': ' ',
    'mL': ' ', 'mM': ' ', 'mR': ' ',
    'bL': ' ', 'bM': ' ', 'bR': ' '
}


def printboard():
    print("Possible moves are:\ntL tM tR\nmL mM mR\nbL bM bR")
    print(tb['tL'] + " | " + tb['tM'] + " | " + tb['tR'] + " | ")
    print("--+---+---+")
    print(tb['mL'] + " | " + tb['mM'] + " | " + tb['mR'] + " | ")
    print("--+---+---+")
    print(tb['bL'] + " | " + tb['bM'] + " | " + tb['bR'] + " | ")
    print("--+---+---+")


print("Welcome to TicTacToe! ", end="")
move = ' '
turn = 'X'
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
    if ((tb['tL'] == tb['tM'] == tb['tR'] and tb['tL'] != ' ' and tb['tM'] != ' ' and tb['tR'] != ' ') or
            (tb['mL'] == tb['mM'] == tb['mR'] and tb['mL'] != ' ' and tb['mM'] != ' ' and tb['mR'] != ' ') or
            (tb['bL'] == tb['bM'] == tb['bR'] and tb['bL'] != ' ' and tb['bM'] != ' ' and tb['bR'] != ' ') or
            (tb['tL'] == tb['mL'] == tb['bL'] and tb['tL'] != ' ' and tb['mL'] != ' ' and tb['bL'] != ' ') or
            (tb['tM'] == tb['mM'] == tb['bM'] and tb['tM'] != ' ' and tb['mM'] != ' ' and tb['bM'] != ' ') or
            (tb['tR'] == tb['mR'] == tb['bR'] and tb['tR'] != ' ' and tb['mR'] != ' ' and tb['bR'] != ' ') or
            (tb['tR'] == tb['mM'] == tb['bL'] and tb['tR'] != ' ' and tb['mM'] != ' ' and tb['bL'] != ' ') or
            (tb['bL'] == tb['mM'] == tb['tR']) and tb['bL'] != ' ' and tb['mM'] != ' ' and tb['tR'] != ' '):
        printboard()
        print("Player " + turn + " wins!")
        break
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    if i == 8:
        print("Game over! Draw!")
