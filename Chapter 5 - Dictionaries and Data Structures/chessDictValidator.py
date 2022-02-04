# Chess Directory Validator
# Chapter 5 - Dictionaries and Data Structures
# Uppercase = white | Lowercase = black
import itertools


def is_valid_board(brd, tests=False):
    wc = 0  # white pieces counter
    bc = 0  # black pieces counter
    blackpawn = 0  # black pawns counter
    whitepawn = 0  # white pawns counter
    # bool values for final if below
    kings = black_count = white_count = black_pawn = white_pawn = square_error = piece_error = False

    # Setting squares_str to check whether the square coordinate is correct (ex. a1, b3, e5)
    sqr_col = "123456789"
    sqr_row = "abcdefgh"
    squares = list(itertools.product(sqr_row, sqr_col))
    squares_str = ""
    for i in range(len(squares)):
        if not i % 9 - 8:
            continue
        squares_str += squares[i][0]
        squares_str += squares[i][1] + " "

    # Now when squares_str is "a1 a2 a3 a4 ... h7 h8" the program checks if dict has correct keys
    for key in brd.keys():
        if square_error is not True:
            if squares_str.find(str(key)) == -1:
                square_error = True

    # Checking whether the pieces set are correct (ex. K, p, r, Q)
    correct_pieces_str = "K k Q q N n R r B b P p"
    for val in brd.values():
        if piece_error is not True:
            if correct_pieces_str.find(val) == -1:
                piece_error = True

    # following are pawn and pieces counters
    for v in brd:
        if 'a' <= brd[v] <= 'z':
            bc += 1
            if 'p' in brd[v]:
                blackpawn += 1
    for v in brd:
        if 'A' <= brd[v] <= 'Z':
            wc += 1
            if 'p' in brd[v]:
                whitepawn += 1

    if 'k' in brd.values() and 'K' in brd.values():
        kings = True  # check if both kings are on board
    if bc < 17:
        black_count = True  # check if there are no more than 16 pieces
    if wc < 17:
        white_count = True
    if blackpawn < 9:
        black_pawn = True  # check if there are no more than 8 pawns
    if whitepawn < 9:
        white_pawn = True

    # List out all the conditions and their values (optional)
    if tests is True:
        print("Kings: " + str(kings) + " (expected: True)")
        print("black_count: " + str(black_count) + " (expected: True)")
        print("white_count: " + str(white_count) + " (expected: True)")
        print("black_pawn: " + str(black_pawn) + " (expected: True)")
        print("white_pawn: " + str(white_pawn) + " (expected: True)")
        print("square_error: " + str(square_error) + " (expected: False)")
        print("piece_error: " + str(piece_error) + " (expected: False)")

    # Aggregate all checks into an if, return true if all conditions are matched (two ifs to fit into 120 char limit)
    if kings is True and black_count is True and white_count is True and black_pawn is True and white_pawn is True:
        if square_error is False and piece_error is False:
            return True
        else:
            return False
    else:
        return False


board = {'h1': 'k', 'c6': 'Q',
         'g2': 'b', 'h5': 'q',
         'e3': 'K', 'e2': 'p'}
incorrect_board = {'h0': 'k', 'c6': 'Q',
                   'g2': 'p', 'h5': 'P',
                   'e3': 'Z', 'e2': 'R'}
print(is_valid_board(board))
print(is_valid_board(incorrect_board, True))
