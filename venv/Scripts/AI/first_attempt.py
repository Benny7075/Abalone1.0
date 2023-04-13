import pygame
import math
import move_pieces
import time
import timeit
import random
import copy
import AI
import hashlib
board = move_pieces.board
starting_board = copy.deepcopy(board)

ROW_COUNT = 15
COLUMN_COUNT = 11

randomlist = []
randomlist.append(random.randint(18, 22))
randomlist.append(random.randint(14, 18))
randomlist.append(random.randint(11, 15))
randomlist.append(random.randint(8, 12))
randomlist.append(random.randint(800, 1200))
randomlist.append(random.randint(700, 1100))

def get_center_value(row, col, randomlist = [], random = False):
    if not random:
        # center
        if row == 7 and col == 5:
            return 2

        # layer 1
        elif (row == 6 or row == 8) and (col == 5 or col == 4):
            return 1.6
        elif row == 7 and (col == 4 or col == 6):
            return 1.6

        # layer 2
        elif (row == 5 or row == 9) and (col == 6 or col == 5 or col == 4):
            return 1.3
        elif (row == 6 or row == 8) and (col == 3 or col == 6):
            return 1.3
        elif row == 7 and (col == 3 or col == 7):
            return 1.3

        # layer 3
        elif (row == 4 or row == 10) and (col == 6 or col == 5 or col == 4 or col == 3):
            return 1
        elif (row == 5 or row == 9) and (col == 7 or col == 3):
            return 1
        elif (row == 6 or row == 8) and (col == 2 or col == 7):
            return 1
        elif row == 7 and (col == 2 or col == 8):
            return 1

        # outer layer
        else:
            return -1
    else:
        # center
        if row == 7 and col == 5:
            return randomlist[0]/10

        # layer 1
        elif (row == 6 or row == 8) and (col == 5 or col == 4):
            return randomlist[1]/10
        elif row == 7 and (col == 4 or col == 6):
            return randomlist[1]/10

        # layer 2
        elif (row == 5 or row == 9) and (col == 6 or col == 5 or col == 4):
            return randomlist[2]/10
        elif (row == 6 or row == 8) and (col == 3 or col == 6):
            return randomlist[2]/10
        elif row == 7 and (col == 3 or col == 7):
            return randomlist[2]/10

        # layer 3
        elif (row == 4 or row == 10) and (col == 6 or col == 5 or col == 4 or col == 3):
            return randomlist[3]/10
        elif (row == 5 or row == 9) and (col == 7 or col == 3):
            return randomlist[3]/10
        elif (row == 6 or row == 8) and (col == 2 or col == 7):
            return randomlist[3]/10
        elif row == 7 and (col == 2 or col == 8):
            return randomlist[3]/10

        # outer layer
        else:
            return -1



def evaluate_pos1(board, piece):
    piececount = 0
    opp_piececount = 0
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    score = 0
    for i in range(3, 12):
        if i == 3 or i == 11:
            for j in range(3, 8):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 * get_center_value(i, j)
        if i == 4 or i == 10:
            for j in range(2, 8):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 * get_center_value(i, j)
        if i == 5 or i == 9:
            for j in range(2, 9):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 * get_center_value(i, j)
        if i == 6 or i == 8:
            for j in range(1, 9):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 * get_center_value(i, j)
        if i == 7:
            for j in range(1, 10):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 * get_center_value(i, j)
    score = score - (14 - piececount)*1000
    score = score + (14 - opp_piececount)*900
    return score

railing = {(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2), (3, 8), (4, 1), (4, 8),
           (5, 1), (5, 9), (6, 0), (6, 9), (7, 0), (7, 10), (8, 0), (8, 9), (9,1), (9, 9),
           (10, 1), (10, 8), (11, 2), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)}


def ball_on_rail(positions, piece):
    global railing
    for marble in positions:
        if marble[0] == piece:
            if (marble[1], marble[2]) in railing:
                return True
    return False



def winning_move(positions, piece):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    if piece == 2:
        if board[14][3] != 50 and ball_on_rail(positions, opp_piece):
            return True
    elif piece == 3:
        if board[0][6] != 60 and ball_on_rail(positions, opp_piece):
            return True

def is_terminal_node(positions):
    return winning_move(positions, 2) or winning_move(positions, 3)


def iterative_deepener(timelimit, board, alpha, beta, piece):
    trans_table = {}
    starttime1 = time.time()
    best_move, score = Minimax(board, 1, alpha, beta, piece, True)
    print(best_move)
    print(score)
    endtime1 = time.time()
    time_passed1 = endtime1 - starttime1

    starttime2 = time.time()
    best_move, score = Minimax(board, 2, alpha, beta, piece, True)
    print(best_move)
    print(score)
    endtime2 = time.time()
    time_passed2 = endtime2 - starttime2
    if time_passed1 != 0:
        ratio = time_passed2 / time_passed1
    else:
        ratio = 1
    time_left = timelimit - time_passed1 - time_passed2
    depth = 3
    while time_left - time_passed2 * ratio > 0:
        starttime3 = time.time()
        best_move, score = AI.Minimax(board, depth, alpha, beta, piece, True)
        endtime3 = time.time()
        time_passed3 = endtime3 - starttime3
        time_left -= time_passed3
        time_passed1 = time_passed2
        time_passed2 = time_passed3
        ratio = time_passed2 / time_passed1
        depth += 1
        print("TRIED ANOTHER DEPTH")
        print(best_move)

    return best_move, score

print(randomlist)

def evaluate_posRandom(board, piece):
    global randomlist
    piececount = 0
    opp_piececount = 0
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    score = 0
    for i in range(3, 12):
        if i == 3 or i == 11:
            for j in range(3, 8):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    piececount += 1
                    score += 100 + get_center_value(i, j, randomlist, True) * 10
                if board [i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 + get_center_value(i, j, randomlist, True) * 10
        if i == 4 or i == 10:
            for j in range(2, 8):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    piececount += 1
                    score += 100 + get_center_value(i, j, randomlist, True) * 10
                if board[i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 + get_center_value(i, j, randomlist, True) * 10
        if i == 5 or i == 9:
            for j in range(2, 9):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    piececount += 1
                    score += 100 + get_center_value(i, j, randomlist, True) * 10
                if board[i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 + get_center_value(i, j, randomlist, True) * 10
        if i == 6 or i == 8:
            for j in range(1, 9):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    piececount += 1
                    score += 100 + get_center_value(i, j, randomlist, True) * 10
                if board[i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 + get_center_value(i, j, randomlist, True) * 10
        if i == 7:
            for j in range(1, 10):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    piececount += 1
                    score += 100 + get_center_value(i, j, randomlist, True) * 10
                if board[i][j] == opp_piece:
                    opp_piececount += 1
                    score -= 100 + get_center_value(i, j, randomlist, True) * 10

    score = score - (14 - piececount) * randomlist[4]
    score = score + (14 - opp_piececount) * randomlist[5]
    return score


# Initialize the Zobrist keys
zobrist_keys = [[0 for j in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]
for i in range(ROW_COUNT):
    for j in range(COLUMN_COUNT):
        zobrist_keys[i][j] = [random.randint(0, 2**64-1), random.randint(0, 2**64-1), random.randint(0, 2**64-1), random.randint(0, 2**64-1)]

def generate_zobrist_key(positions):
    """
    Generates a Zobrist key for the given board state.
    """
    key = 0
    for marble in positions:
        piece_index = marble[0] - 2
        key ^= zobrist_keys[marble[1]][marble[2]][piece_index]
    return key