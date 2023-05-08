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


def check_winner(tb):
    # Check rows
    for row in ['t', 'm', 'b']:
        if tb[row + 'L'] == tb[row + 'M'] == tb[row + 'R'] != ' ':
            return True

    # Check columns
    for col in ['L', 'M', 'R']:
        if tb['t' + col] == tb['m' + col] == tb['b' + col] != ' ':
            return True

    # Check diagonals
    if tb['tL'] == tb['mM'] == tb['bR'] != ' ' or tb['tR'] == tb['mM'] == tb['bL'] != ' ':
        return True

    return False


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
    if check_winner(tb):
        printboard()
        print("Player " + turn + " wins!")
        break
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    if i == 8:
        print("Game over! Draw!")
