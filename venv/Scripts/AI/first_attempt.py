import pygame
import math
import move_pieces
import time
import timeit
import random
import copy
import AI
board = move_pieces.board
starting_board = copy.deepcopy(board)

def get_center_value(row, col):
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
        return 0.4


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
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    score -= 100 * get_center_value(i, j)
        if i == 4 or i == 10:
            for j in range(2, 8):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    score -= 100 * get_center_value(i, j)
        if i == 5 or i == 9:
            for j in range(2, 9):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    score -= 100 * get_center_value(i, j)
        if i == 6 or i == 8:
            for j in range(1, 9):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    score -= 100 * get_center_value(i, j)
        if i == 7:
            for j in range(1, 10):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    score += 100 * get_center_value(i, j)
                if board [i][j] == opp_piece:
                    score -= 100 * get_center_value(i, j)
        if ball_on_rail(board, opp_piece):
            score += 600
        if ball_on_rail(board, piece):
            score -= 500
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
                return None, 0
        else:
            return None, evaluate_pos1(board, piece)
    valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, piece, opp_piece)
    if move != -1:
        if move in valid_moves:
            valid_moves.remove(move)
    if maximising:
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
  #          start = time.time()
            b_copy = board.copy()
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
            new_score = Minimax(b_copy, depth - 1, alpha, beta, piece, False)[1]
      #      end = time.time()
       #     print(end - start)


 #           board, knock_off, row, col = AI.play_move(board, move, piece, opp_piece)
  #          new_score = Minimax(board, depth - 1, alpha, beta, piece, False)[1]
   #         board = AI.undo_move(board, move, piece, opp_piece)
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
            b_copy = board.copy()
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
            new_score = Minimax(b_copy, depth - 1,alpha, beta, piece, True)[1]
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value

def Minimax2(board, depth, alpha, beta, piece, maximising, move = -1):
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
                return None, 0
        else:
            return None, evaluate_pos2(board, piece)
    valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(board, piece, opp_piece)
    if move == -1:
        pass
    else:
        if move in valid_moves:
            valid_moves.remove(move)
    if maximising:
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
            b_copy = board.copy()
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
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
        return best_move, value

    else:
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
            b_copy = board.copy() # rather than making a copy each time theres talk of an undo move function...
            b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
            new_score = Minimax2(b_copy, depth - 1,alpha, beta, piece, True)[1]
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value


def evaluate_pos2(board, piece):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    score = 0
    for i in range(3, 12):
        if i == 3 or i == 11:
            for j in range(3, 8):
                if board[i][j] == piece or board[i][j] == 10*piece:
                    score += 100 + get_center_value(i, j) * 10
                if board [i][j] == opp_piece:
                    score -= 100 + get_center_value(i, j) * 10
        if i == 4 or i == 10:
            for j in range(2, 8):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    score += 100 + get_center_value(i, j) * 10
                if board[i][j] == opp_piece:
                    score -= 100 + get_center_value(i, j) * 10
        if i == 5 or i == 9:
            for j in range(2, 9):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    score += 100 + get_center_value(i, j) * 10
                if board[i][j] == opp_piece:
                    score -= 100 + get_center_value(i, j) * 10
        if i == 6 or i == 8:
            for j in range(1, 9):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    score += 100 + get_center_value(i, j) * 10
                if board[i][j] == opp_piece:
                    score -= 100 + get_center_value(i, j) * 10
        if i == 7:
            for j in range(1, 10):
                if board[i][j] == piece or board[i][j] == 10 * piece:
                    score += 100 + get_center_value(i, j) * 10
                if board[i][j] == opp_piece:
                    score -= 100 + get_center_value(i, j) * 10

    return score