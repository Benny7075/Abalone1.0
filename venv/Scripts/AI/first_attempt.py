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

def ball_on_rail(board, piece):
    for j in range(2, 8):
        if board[2][j] == piece:
            return True
        if board[12][j] == piece:
            return True
    if board[3][2] == piece or board[3][8] == piece:
        return True
    if board[4][1] == piece or board[4][8] == piece:
        return True
    if board[5][1] == piece or board[5][9] == piece:
        return True
    if board[6][0] == piece or board[6][9] == piece:
        return True
    if board[7][0] == piece or board[7][10] == piece:
        return True
    if board[8][0] == piece or board[8][9] == piece:
        return True
    if board[9][1] == piece or board[9][9] == piece:
        return True
    if board[10][1] == piece or board[10][8] == piece:
        return True
    if board[11][2] == piece or board[11][8] == piece:
        return True

    return False



def winning_move(board, piece):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    if piece == 2:
        if board[14][3] != 50 and ball_on_rail(board, opp_piece):
            return True
    elif piece == 3:
        if board[0][6] != 60 and ball_on_rail(board, opp_piece):
            return True

def is_terminal_node(board):
    return winning_move(board, 2) or winning_move(board, 3)

times = 0
times2 = 0
def Minimax(board, depth, alpha, beta, piece, maximising, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal_node(board):
        if is_terminal:
            if winning_move(board, piece):
                return None, 9999999999
            elif winning_move(board, opp_piece):
                return None, -9999999999
        else:
            global times
            times += 1
            print("evaluated this many times: " + str(times))
         #   return None, evaluate_posRandom(board, piece)
            return None, evaluate_pos1(board, piece)
    if maximising:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, piece, opp_piece)
        if move != -1:
            if move in valid_moves:
                valid_moves.remove(move)
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
     #       b_copy = board.copy()
      #      b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
       #     new_score = Minimax(b_copy, depth - 1, alpha, beta, piece, False)[1]

            board, knock_off, row, col = AI.play_move(board, move, piece, opp_piece)
            new_score = Minimax(board, depth - 1, alpha, beta, piece, False)[1]
            board = AI.undo_move(board, move, piece, opp_piece)
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, opp_piece, piece)
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
    #        b_copy = board.copy()
     #       b_copy, knock_off, row, col = AI.play_move(b_copy, move, opp_piece, piece)
      #      new_score = Minimax(b_copy, depth - 1,alpha, beta, piece, True)[1]

            board, knock_off, row, col = AI.play_move(board, move, opp_piece, piece)
            new_score = Minimax(board, depth - 1, alpha, beta, piece, True)[1]
            board = AI.undo_move(board, move, opp_piece, piece)
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value


def get_state_key(board):
    # Convert the board to a string
    board_str = str(board)

    # Generate a SHA-256 hash of the string
    hash_obj = hashlib.sha256(board_str.encode())
    hash_str = hash_obj.hexdigest()

    return hash_str

def Minimax2(board, depth, alpha, beta, piece, maximising, move = -1, trans_table={}):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal_node(board):
        if is_terminal:
            if winning_move(board, piece):
                return None, 9999999999
            elif winning_move(board, opp_piece):
                return None, -9999999999
        else:
            pos_score = evaluate_pos1(board, piece)
            # Generate state key for current board state
     #       state_key = get_state_key(board)
      #      trans_table[state_key] = pos_score
            return None, pos_score
    if maximising:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, piece, opp_piece)
        if move == -1:
            pass
        else:
            if move in valid_moves:
                valid_moves.remove(move)
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
            b_copy = board.copy()
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
            state_key = get_state_key(b_copy)
            if state_key in trans_table:
                new_score = trans_table[state_key]
            else:
                new_score = Minimax2(b_copy, depth - 1, alpha, beta, piece, False)[1]
       #     if move in valid_knocks:
        #        print(move)
         #       return move, -1
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        result = best_move, value

    else:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, opp_piece, piece)
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
            b_copy = board.copy()
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, opp_piece, piece)
            state_key = get_state_key(b_copy)
            if state_key in trans_table:
                new_score = trans_table[state_key]
            else:
                new_score = Minimax2(b_copy, depth - 1, alpha, beta, piece, True)[1]
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        result = best_move, value

    return result


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


def Minimax3(board, depth, alpha, beta, piece, maximising, zobrist_table, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal_node(board):
        if is_terminal:
            if winning_move(board, piece):
                return None, 9999999999
            elif winning_move(board, opp_piece):
                return None, -9999999999
        else:
            pos_score = evaluate_pos1(board, piece)
            key = generate_zobrist_key(board)
            zobrist_table[key] = None, pos_score
            global times2
            times2 += 1
            print("evaluated this many times with hashmap: " + str(times2))
        #    return None, evaluate_posRandom(board, piece)
            return None, pos_score
    if maximising:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, piece, opp_piece)
        if move != -1:
            if move in valid_moves:
                valid_moves.remove(move)
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
     #       b_copy = board.copy()
      #      b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
       #     new_score = Minimax3(b_copy, depth - 1, alpha, beta, piece, False)[1]

            board, knock_off, row, col = AI.play_move(board, move, piece, opp_piece)
        # Look up the Zobrist key for the board state
            board_key = generate_zobrist_key(board)
            if board_key in zobrist_table:
                new_score = zobrist_table[board_key][1]
            new_score = Minimax3(board, depth - 1, alpha, beta, piece, False, zobrist_table)[1]
            board = AI.undo_move(board, move, piece, opp_piece)
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, opp_piece, piece)
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
    #        b_copy = board.copy()
    #        b_copy, knock_off, row, col = AI.play_move(b_copy, move, opp_piece, piece)
     #       new_score = Minimax3(b_copy, depth - 1,alpha, beta, piece, True)[1]

            board, knock_off, row, col = AI.play_move(board, move, opp_piece, piece)
             # Look up the Zobrist key for the board state
            board_key = generate_zobrist_key(board)
            if board_key in zobrist_table:
                new_score = zobrist_table[board_key][1]
            else:
                new_score = Minimax3(board, depth - 1, alpha, beta, piece, True, zobrist_table)[1]
            board = AI.undo_move(board, move, opp_piece, piece)
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value


# Initialize the Zobrist keys
zobrist_keys = [[0 for j in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]
for i in range(ROW_COUNT):
    for j in range(COLUMN_COUNT):
        zobrist_keys[i][j] = [random.randint(0, 2**64-1), random.randint(0, 2**64-1)]

def generate_zobrist_key(board):
    """
    Generates a Zobrist key for the given board state.
    """
    key = 0
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            piece = board[i][j]
            if piece == 2 or piece == 3:
                piece_index = int(piece - 2)
                key ^= zobrist_keys[i][j][piece_index]
    return key