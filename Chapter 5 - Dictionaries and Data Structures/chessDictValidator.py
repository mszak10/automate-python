# Chess Directory Validator
# Chapter 5 - Dictionaries and Data Structures
# Uppercase = white | Lowercase = black
import itertools

board = {'h1': 'k', 'c6': 'Q',
         'g2': 'b', 'h5': 'q', 'e3': 'K', 'e2': 'p'}


def isValidChessBoard():
    wc = 0  # white pieces counter
    bc = 0  # black pieces counter
    blackpawn = 0  # black pawns counter
    whitepawn = 0  # white pawns counter
    sqrCol = "123456789"
    sqrRow = "abcdefgh"
    squares = list(itertools.product(sqrRow, sqrCol))
    for v in board:
        if 'a' <= board[v] <= 'z':
            bc += 1
            if 'p' in board[v]:
                blackpawn += 1
    for v in board:
        if 'A' <= board[v] <= 'Z':
            wc += 1
            if 'p' in board[v]:
                whitepawn += 1
    print(squares)

    if 'k' in board and 'K' in board: kings = True
    if bc < 17: blackCount = True
    if wc < 17: whiteCount = True
    if blackpawn < 9: blackPawn = True
    if whitepawn < 9: whitePawn = True
    # print(str(sqrCol[0]) + sqrRow[0])
    print(squares[0])  # TODO: finishing for the night - turn ('a', '1'), ('a', '2'), into 'a1', 'a2'


isValidChessBoard()
