import pygame
import math
import move_pieces
import time
import timeit
import random
import copy
import AI
import hashlib


def Minimax(board, depth, alpha, beta, piece, maximising, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = AI.is_terminal_node(board)
    if depth == 0 or AI.is_terminal_node(board):
        if is_terminal:
            if AI.winning_move(board, piece):
                return None, 9999999999
            elif AI.winning_move(board, opp_piece):
                return None, -9999999999
        else:
         #   return None, evaluate_posRandom(board, piece)
            return None, AI.evaluate_pos1(board, piece)
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


def Minimax3(board, depth, alpha, beta, piece, maximising, zobrist_table, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = AI.is_terminal_node(board)
    if depth == 0 or AI.is_terminal_node(board):
        if is_terminal:
            if AI.winning_move(board, piece):
                return None, 9999999999
            elif AI.winning_move(board, opp_piece):
                return None, -9999999999
        else:
            pos_score = AI.evaluate_pos1(board, piece)
            key = AI.generate_zobrist_key(board)
            zobrist_table[key] = None, pos_score
            timetest += 1
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
            board_key = AI.generate_zobrist_key(board)
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
            board_key = AI.generate_zobrist_key(board)
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
