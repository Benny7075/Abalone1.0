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

center_values = {
        (7, 5): 2,
        (6, 5): 1.6, (8, 5): 1.6, (7, 4): 1.6, (7, 6): 1.6, (6, 4): 1.6, (8, 4): 1.6,
        (5, 6): 1.3, (9, 6): 1.3, (5, 5): 1.3, (9, 5): 1.3, (7, 7): 1.3,
        (5, 4): 1.3, (9, 4): 1.3, (6, 3): 1.3, (8, 3): 1.3, (6, 6): 1.3, (8, 6): 1.3,
        (7, 3): 1.3, (4, 6): 1, (10, 6): 1, (4, 5): 1,
        (10, 5): 1, (4, 4): 1, (10, 4): 1, (4, 3): 1,
        (10, 3): 1, (5, 7): 1, (9, 7): 1, (6, 2): 1,
        (8, 2): 1, (7, 2): 1, (9, 3): 1, (5, 3): 1, (6, 7): 1, (8, 7): 1, (7, 8): 1
    }

random_centers = {
        (7, 5): randomlist[0]/10,
        (6, 5): randomlist[1]/10, (8, 5): randomlist[1]/10, (7, 4): randomlist[1]/10, (7, 6): randomlist[1]/10, (6, 4): randomlist[1]/10, (8, 4): randomlist[1]/10,
        (5, 6): randomlist[2]/10, (9, 6): randomlist[2]/10, (5, 5): randomlist[2]/10, (9, 5): randomlist[2]/10, (7, 7): randomlist[2]/10,
        (5, 4): randomlist[2]/10, (9, 4): randomlist[2]/10, (6, 3): randomlist[2]/10, (8, 3): randomlist[2]/10, (6, 6): randomlist[2]/10, (8, 6): randomlist[2]/10,
        (7, 3): randomlist[2]/10, (4, 6): randomlist[3]/10, (10, 6): randomlist[3]/10, (4, 5): randomlist[3]/10,
        (10, 5): randomlist[3]/10, (4, 4): randomlist[3]/10, (10, 4): randomlist[3]/10, (4, 3): randomlist[3]/10,
        (10, 3): randomlist[3]/10, (5, 7): randomlist[3]/10, (9, 7): randomlist[3]/10, (6, 2): randomlist[3]/10,
        (8, 2): randomlist[3]/10, (7, 2): randomlist[3]/10, (9, 3): randomlist[3]/10, (5, 3): randomlist[3]/10, (6, 7): randomlist[3]/10, (8, 7): randomlist[3]/10, (7, 8): randomlist[3]/10
}

def get_center_value(row, col, random = False):
    if not random:
        return center_values.get((row, col), -1)
    else:
        return random_centers.get((row, col), -1)



def evaluate_pos1(board, piece):

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