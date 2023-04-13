import numpy
import pygame
import sys
import math
import random
import move_pieces
import start_and_menu
import AI
import copy
import time
pygame.init()

boards = []
def get_boards_in_list(boards):
    boardLevels = move_pieces.create_boardLevels()
    boards.append(boardLevels)
    board1 = move_pieces.create_board1()
    boards.append(board1)
    board2 = move_pieces.create_board2()
    boards.append(board2)
    board3 = move_pieces.create_board3()
    boards.append(board3)
    board4 = move_pieces.create_board4()
    boards.append(board4)
    board5 = move_pieces.create_board5()
    boards.append(board5)
    board6 = move_pieces.create_board6()
    boards.append(board6)
    board7 = move_pieces.create_board7()
    boards.append(board7)
    board8 = move_pieces.create_board8()
    boards.append(board8)
    board9 = move_pieces.create_board9()
    boards.append(board9)
    board10 = move_pieces.create_board10()
    boards.append(board10)
    board11 = move_pieces.create_board11()
    boards.append(board11)
    board12 = move_pieces.create_board12()
    boards.append(board12)
    board13 = move_pieces.create_board13()
    boards.append(board13)
    board14 = move_pieces.create_board14()
    boards.append(board14)
    board15 = move_pieces.create_board15()
    boards.append(board15)
    board16 = move_pieces.create_board16()
    boards.append(board16)
    board17 = move_pieces.create_board17()
    boards.append(board17)
    board18 = move_pieces.create_board18()
    boards.append(board18)
    board19 = move_pieces.create_board19()
    boards.append(board19)
    board20 = move_pieces.create_board20()
    boards.append(board20)
    board21 = move_pieces.create_board21()
    boards.append(board21)
    board22 = move_pieces.create_board22()
    boards.append(board22)
    board23 = move_pieces.create_board23()
    boards.append(board23)
    board24 = move_pieces.create_board24()
    boards.append(board24)
    board25 = move_pieces.create_board25()
    boards.append(board25)
    board26 = move_pieces.create_board26()
    boards.append(board26)
    board27 = move_pieces.create_board27()
    boards.append(board27)
    board28 = move_pieces.create_board28()
    boards.append(board28)
    board29 = move_pieces.create_board29()
    boards.append(board29)
    board30 = move_pieces.create_board30()
    boards.append(board30)
    board31 = move_pieces.create_board31()
    boards.append(board31)
    board32 = move_pieces.create_board32()
    boards.append(board32)
    board33 = move_pieces.create_board33()
    boards.append(board33)
    board34 = move_pieces.create_board34()
    boards.append(board34)
    board35 = move_pieces.create_board35()
    boards.append(board35)
    board36 = move_pieces.create_board36()
    boards.append(board36)
    board37 = move_pieces.create_board37()
    boards.append(board37)
    board38 = move_pieces.create_board38()
    boards.append(board38)
    board39 = move_pieces.create_board39()
    boards.append(board39)
    board40 = move_pieces.create_board40()
    boards.append(board40)
    board41 = move_pieces.create_board41()
    boards.append(board41)
    board42 = move_pieces.create_board42()
    boards.append(board42)
    board43 = move_pieces.create_board43()
    boards.append(board43)
    board44 = move_pieces.create_board44()
    boards.append(board44)
    board45 = move_pieces.create_board45()
    boards.append(board45)
    board46 = move_pieces.create_board46()
    boards.append(board46)
    board47 = move_pieces.create_board47()
    boards.append(board47)
    board48 = move_pieces.create_board48()
    boards.append(board48)
    board49 = move_pieces.create_board49()
    boards.append(board49)
    board50 = move_pieces.create_board50()
    boards.append(board50)
    board51 = move_pieces.create_board51()
    boards.append(board51)
    board52 = move_pieces.create_board52()
    boards.append(board52)
    board53 = move_pieces.create_board53()
    boards.append(board53)
    board54 = move_pieces.create_board54()
    boards.append(board54)
    board55 = move_pieces.create_board55()
    boards.append(board55)
    board56 = move_pieces.create_board56()
    boards.append(board56)
    board57 = move_pieces.create_board57()
    boards.append(board57)
    board58 = move_pieces.create_board58()
    boards.append(board58)
    board59 = move_pieces.create_board59()
    boards.append(board59)
    board60 = move_pieces.create_board60()
    boards.append(board60)
    board61 = move_pieces.create_board61()
    boards.append(board61)

get_boards_in_list(boards)

def get_level_from_board(row, col):
    if (row, col) == (3, 3):
        return 1
    if (row, col) == (3, 4):
        return 2
    if (row, col) == (3, 5):
        return 3
    if (row, col) == (3, 6):
        return 4
    if (row, col) == (3, 7):
        return 5
    if (row, col) == (4, 2):
        return 6
    if (row, col) == (4, 3):
        return 7
    if (row, col) == (4, 4):
        return 8
    if (row, col) == (4, 5):
        return 9
    if (row, col) == (4, 6):
        return 10
    if (row, col) == (4, 7):
        return 11
    if (row, col) == (5, 2):
        return 12
    if (row, col) == (5, 3):
        return 13
    if (row, col) == (5, 4):
        return 14
    if (row, col) == (5, 5):
        return 15
    if (row, col) == (5, 6):
        return 16
    if (row, col) == (5, 7):
        return 17
    if (row, col) == (5, 8):
        return 18
    if (row, col) == (6, 1):
        return 19
    if (row, col) == (6, 2):
        return 20
    if (row, col) == (6, 3):
        return 21
    if (row, col) == (6, 4):
        return 22
    if (row, col) == (6, 5):
        return 23
    if (row, col) == (6, 6):
        return 24
    if (row, col) == (6, 7):
        return 25
    if (row, col) == (6, 8):
        return 26
    if (row, col) == (7, 1):
        return 27
    if (row, col) == (7, 2):
        return 28
    if (row, col) == (7, 3):
        return 29
    if (row, col) == (7, 4):
        return 30
    if (row, col) == (7, 5):
        return 31
    if (row, col) == (7, 6):
        return 32
    if (row, col) == (7, 7):
        return 33
    if (row, col) == (7, 8):
        return 34
    if (row, col) == (7, 9):
        return 35
    if (row, col) == (8, 1):
        return 36
    if (row, col) == (8, 2):
        return 37
    if (row, col) == (8, 3):
        return 38
    if (row, col) == (8, 4):
        return 39
    if (row, col) == (8, 5):
        return 40
    if (row, col) == (8, 6):
        return 41
    if (row, col) == (8, 7):
        return 42
    if (row, col) == (8, 8):
        return 43
    if (row, col) == (9, 2):
        return 44
    if (row, col) == (9, 3):
        return 45
    if (row, col) == (9, 4):
        return 46
    if (row, col) == (9, 5):
        return 47
    if (row, col) == (9, 6):
        return 48
    if (row, col) == (9, 7):
        return 49
    if (row, col) == (9, 8):
        return 50
    if (row, col) == (10, 2):
        return 51
    if (row, col) == (10, 3):
        return 52
    if (row, col) == (10, 4):
        return 53
    if (row, col) == (10, 5):
        return 54
    if (row, col) == (10, 6):
        return 55
    if (row, col) == (10, 7):
        return 56
    if (row, col) == (11, 3):
        return 57
    if (row, col) == (11, 4):
        return 58
    if (row, col) == (11, 5):
        return 59
    if (row, col) == (11, 6):
        return 60
    if (row, col) == (11, 7):
        return 61
    return -1

def get_board_from_level(level):
    for i in range(62):
        if i == level:
            if level < 6:
                return 3, 2 + i
            if level >= 6 and level < 12:
                return 4, i - 4
            if level >= 12 and level < 19:
                return 5, i - 10
            if level >= 19 and level < 27:
                return 6, i - 17
            if level >= 27 and level < 36:
                return 7, i - 25
            if level >= 36 and level < 44:
                return 8, i - 34
            if level >= 44 and level < 51:
                return 9, i - 42
            if level >= 51 and level < 57:
                return 10, i - 49
            if level >= 57:
                return 11, i - 55

oppliveslist = []
oppliveslist = move_pieces.get_opp_lives(oppliveslist)

playerliveslist = []
playerliveslist = move_pieces.get_player_lives(playerliveslist)

timeslist = []
timeslist = move_pieces.get_level_times(timeslist)

depthlist = []
depthlist = move_pieces.get_AIlevel(depthlist)

def adjust_board_for_lives_player(board, lives):
    if lives == 1:
        for i in range(2, 7):
            board[0][i] = 101
    if lives == 2:
        for i in range(2, 6):
            board[0][i] = 101
    if lives == 3:
        for i in range(2, 5):
            board[0][i] = 101
    if lives == 4:
        for i in range(2, 4):
            board[0][i] = 101
    if lives == 5:
        board[0][2] = 101

def adjust_board_for_lives_opp(board, lives):
    if lives == 1:
        for i in range(3, 8):
            board[14][i] = 101
    if lives == 2:
        for i in range(4, 8):
            board[14][i] = 101
    if lives == 3:
        for i in range(5, 8):
            board[14][i] = 101
    if lives == 4:
        for i in range(6, 8):
            board[14][i] = 101
    if lives == 5:
        board[14][7] = 101

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
LGREY = [120,120,120]
DGREY = [50,50,50]
DDGREY = [30,30,30]
YELLOW = [195,190,54]
GREEN = [116,209,106]
BLUE = [106, 164, 209]
RED = [255,50,50]
LRED = [255, 110, 100]
ROW_COUNT = 15
COLUMN_COUNT = 11

def print_board(board):
    print(board)

board = move_pieces.create_board()
starting_board = copy.deepcopy(board)
# GUI
SQUARESIZE = 48
RADIUS = int(SQUARESIZE/2 - 5)
TROTH_RAD = int(SQUARESIZE/2 - 5)
HIGH_RAD = int(SQUARESIZE/2)
SMALL_RAD = 10
DOT = 8
width = COLUMN_COUNT * SQUARESIZE
height = ROW_COUNT * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)
screen.fill(DGREY)
pygame.display.update()


global time_delay
global knocked_needs_reset
time_delay = False
knocked_needs_reset = False



def check_movable_piece(board, row, col, piece):
    return board[row][col] == piece

def highlight(board, row, col, piece):
    if board[row][col] == piece:
        board[row][col] = 10 * piece

def unhighlight(board, row, col, piece):
    if board[row][col] == piece:
        board[row][col] = piece/10


def clean_board(board):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 6 or board[r][c] == 7 or board[r][c] == 8:
                board[r][c] = 1
            if starting_board[r][c] == 9 or starting_board[r][c] == 0 and not (board[r][c] == 200 or board[r][c] == 300):
                board[r][c] = starting_board[r][c]



def get_board_pos(posx, posy):
    r = int(math.floor((posy - (0.5*SQUARESIZE))/(0.866*SQUARESIZE)))
    if move_pieces.slanted_row(r):
        COL_POS = int(math.floor((posx + (SQUARESIZE/2))/ SQUARESIZE)) - 1
    else:
        COL_POS = int(math.floor(posx / SQUARESIZE))
    return r, COL_POS


def get_screen_pos(row, col):
    posy = SQUARESIZE + 0.866*SQUARESIZE*row
    if move_pieces.slanted_row(row):
        posx = SQUARESIZE + col*SQUARESIZE
    else:
        posx = (SQUARESIZE/2) + SQUARESIZE*col
    return posx, posy



def drop_piece(board, row, col, piece):
    if board[row][col] == 1 or board[row][col] == 7 or shoving:
        board[row][col] = piece

# dont want to move these because of getting_pushed
getting_pushed = []
def show_pushes2(board, highlighted, opp_piece):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    cmax = max(c1, c2)
    cmin = min(c1, c2)
    res = [0,1,9]
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1 and move_pieces.selectable3(r, c, highlighted):
                board[r][c] = 6
            if board[r][c] == opp_piece and move_pieces.selectable3(r, c, highlighted):
                # patch for weird bug
                if r1 == r2 and board[r1][cmin - 1] == opp_piece and board[r1][cmax + 1] == 1:
                    board[r1][cmax + 1] = 6
                # row case
                if r1 == r2 and board[r1][cmin - 1] == opp_piece and board[r1][cmax + 1] == opp_piece:
                    if board[r1][cmin - 2] in res:
                        board[r1][cmin - 2] = 8
                        getting_pushed.append((r,cmin - 1))
                    if board[r1][cmax + 2] in res:
                        getting_pushed.append((r, cmax + 1))
                        board[r1][cmax + 2] = 8
                else:
                    if (abs(r1 - r) + abs(c1 - c) < abs(r2 - r) + abs(c2 - c)):
                        closest = highlighted[0]
                    else:
                        closest = highlighted[1]
                    getting_pushed.append((r, c))
                    shoved = (r, c)
                    poss_push = [shoved, closest]
                    # probably not the fastest
                    for r in range(ROW_COUNT):
                        for c in range(COLUMN_COUNT):
                            if move_pieces.selectable3(r, c, poss_push) and (board[r][c] == 0 or board[r][c] == 1 or board[r][c] == 9):
                                board[r][c] = 8


def show_pushes3(board, highlighted, opp_piece):
    moving_piece_rows = []
    moving_piece_cols = []
    for counter in highlighted:
        moving_piece_rows.append(counter[0])
        moving_piece_cols.append(counter[1])
    highest_row = min(moving_piece_rows)
    lowest_row = max(moving_piece_rows)
    highest_col = max(moving_piece_cols)
    lowest_col = min(moving_piece_cols)
    index_high = moving_piece_rows.index(highest_row)
    index_low = moving_piece_rows.index(lowest_row)
    mid_row = lowest_row
    for row in moving_piece_rows:
        if row != highest_row and row != lowest_row:
            mid_row = row
    index_mid = moving_piece_rows.index(mid_row)
    r3, c3 = highlighted[0]
    r2, c2 = highlighted[1]
    r1, c1 = highlighted[2]
    cmin = min(c1, c2, c3)
    cmax = max(c1, c2, c3)
    res = [1,0,9]
    first_pair = [highlighted[0], highlighted[1]]
    second_pair = [highlighted[1], highlighted[2]]
    if highest_row != lowest_row:
        first_pair = [(lowest_row, moving_piece_cols[index_low]), (mid_row, moving_piece_cols[index_mid])]
        second_pair = [(mid_row, moving_piece_cols[index_mid]), (highest_row, moving_piece_cols[index_high])]
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1 and (move_pieces.selectable3(r, c, first_pair) or move_pieces.selectable3(r, c, second_pair)):
                board[r][c] = 6
            if board[r][c] == opp_piece and (move_pieces.selectable3(r, c, first_pair) or move_pieces.selectable3(r, c, second_pair)):
                # patch for weird bug
                if r1 == r2 and board[r1][cmin - 1] == opp_piece and board[r1][cmax + 1] in res:
                    if board[r1][cmax + 1] == 1:
                        board[r1][cmax + 1] = 6
                # row case
                if r1 == r2 and (board[r1][cmin - 1] == opp_piece and board[r1][cmax + 1] != opp_piece):
                    if board[r1][cmin - 2] in res:
                        board[r1][cmin - 2] = 8
                        getting_pushed.append((r,cmin - 1))
                    if board[r1][cmin - 2] == opp_piece:
                        if board[r1][cmin - 3] in res:
                            board[r1][cmin - 3] = 8
                            getting_pushed.append((r, cmin - 1))
                elif r1 == r2 and (board[r1][cmin - 1] != opp_piece and board[r1][cmax + 1] == opp_piece):
                    print(cmax)
                    print(cmin)
                    if board[r1][cmax + 2] in res:
                        board[r1][cmax + 2] = 8
                        getting_pushed.append((r1, cmax + 1))
                    if board[r1][cmax + 2] == opp_piece:
                        if board[r1][cmax + 3] in res:
                            board[r1][cmax + 3] = 8
                            getting_pushed.append((r1, cmax + 1))
                elif r1 == r2 and (board[r1][cmin - 1] == opp_piece and board[r1][cmax + 1] == opp_piece):
                    if board[r1][cmin - 2] in res:
                        board[r1][cmin - 2] = 8
                        getting_pushed.append((r,cmin - 1))
                    elif board[r1][cmin - 2] == opp_piece:
                        if board[r1][cmin - 3] in res:
                            board[r1][cmin - 3] = 8
                            getting_pushed.append((r, cmin - 1))
                    if board[r1][cmax + 2] in res:
                        getting_pushed.append((r, cmax + 1))
                        board[r1][cmax + 2] = 8
                    if board[r1][cmax + 2] == opp_piece:
                        if board[r1][cmax + 3] in res:
                            board[r1][cmax + 3] = 8
                            getting_pushed.append((r, cmax + 1))
                else:
                    if (abs(lowest_row - r) + abs(moving_piece_cols[index_low] - c) < abs(highest_row - r) + abs(moving_piece_cols[index_high] - c)):
                        closest = (lowest_row, moving_piece_cols[index_low])
                    else:
                        closest = (highest_row, moving_piece_cols[index_high])
                    shoved = (r, c)
                    getting_pushed.append((r, c))
                    poss_push = [shoved, closest]
                    # probably not the fastest
                    for r in range(ROW_COUNT):
                        for c in range(COLUMN_COUNT):
                            if move_pieces.selectable3(r, c, poss_push) and (board[r][c] == 0 or board[r][c] == 1 or board[r][c] == 9):
                                board[r][c] = 8
                            if move_pieces.selectable3(r, c, poss_push) and (board[r][c] == opp_piece):
                                shoved2 = (r, c)
                                opp_chain = [shoved, shoved2]
                                for r in range(ROW_COUNT):
                                    for c in range(COLUMN_COUNT):
                                        if move_pieces.selectable3(r, c, opp_chain) and (board[r][c] == 0 or board[r][c] == 1 or board[r][c] == 9):
                                            board[r][c] = 8



def knocked_off(board, row, col, piece):
    board[row][col] = 100*piece
    posx, posy = get_screen_pos(row, col)
    circle_center = (posx, posy)
    for i in range(2, 8):
        j = 9 - i
        if piece == 2:
            if board[0][i] == 60:
                board[0][i] = 200
                move_pieces.move_round_edge(screen, circle_center, 2)
                move_pieces.see_us_home(screen, get_screen_pos(2, 7), get_screen_pos(0, i), 2)
                break
        if piece == 3:
            if board[14][j] == 50:
                board[14][j] = 300
                move_pieces.move_round_edge(screen, circle_center, 3)
                move_pieces.see_us_home(screen, get_screen_pos(12, 2), get_screen_pos(14, j), 3)
                break

def make_selection(board, row, col, highlighted, piece):
    if board[row][col] == piece:
        if len(highlighted) == 0:
            highlight(board, row, col, piece)
            if (row, col) not in highlighted:
                highlighted.append((row, col))
        elif len(highlighted) == 1:
            if move_pieces.selectable2(row, col, highlighted):
                highlight(board, row, col, piece)
                highlighted.append((row, col))
        elif len(highlighted) == 2:
            if move_pieces.selectable3(row, col, highlighted):
                highlight(board, row, col, piece)
                highlighted.append((row, col))

knock_off = False
def take_turn(board, row, col, highlighted, getting_pushed, piece):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    if board[row][col] == 6:
        move_pieces.push_piece(board, row, col, highlighted, piece)
        return 4
    if board[row][col] == 7:
        if len(highlighted) == 2:
            if move_pieces.slide_piece2(board, row, col, highlighted, piece):
                for value in highlighted:
                    board[value[0]][value[1]] = 1
                return 4
        if len(highlighted) == 3:
            if move_pieces.slide_piece3(board, row, col, highlighted, piece):
                for value in highlighted:
                    board[value[0]][value[1]] = 1
                return 4
    if board[row][col] == 8:
        move_pieces.shove_piece(board, row, col, highlighted, piece)
        if len(getting_pushed) == 1:
            for value in getting_pushed:
                board[value[0]][value[1]] = piece
        # possible push on either side
        if len(getting_pushed) == 2:
            r1, c1 = getting_pushed[0]
            r2, c2 = getting_pushed[1]
            cmax = max(c1, c2)
            cmin = min(c1, c2)
            # row case
            if r1 == r2:
                if col > cmax:
                    board[r1][cmax] = piece
                if col < cmin:
                   board[r1][cmin] = piece
            else:
                if (abs(r1 - row) + abs(c1 - col) < abs(r2 - row) + abs(c2 - col)):
                    closest = getting_pushed[0]
                else:
                    closest = getting_pushed[1]
                board[closest[0]][closest[1]] = piece
        board[row][col] = opp_piece
        if starting_board[row][col] == 0 or starting_board[row][col] == 9:
            return 5
        getting_pushed = []
        return 4
    return 0

center_values = {(7, 5): 2,
                 (6, 5): 1.6, (6, 4): 1.6, (8, 5): 1.6, (8, 4): 1.6, (7, 4): 1.6, (7, 6): 1.6,
                 (5, 6): 1.3, (9, 6): 1.3, (5, 5): 1.3, (9, 5): 1.3,
                 (5, 4): 1.3, (9, 4): 1.3, (6, 3): 1.3, (8, 3): 1.3,
                 (7, 3): 1.3, (7, 7): 1.3, (6, 6): 1.3, (8, 6): 1.3,
                 (4, 6): 1, (10, 6): 1, (4, 5): 1, (10, 5): 1,
                 (4, 4): 1, (10, 4): 1, (4, 3): 1, (10, 3): 1,
                 (5, 7): 1, (9, 7): 1, (5, 3): 1, (9, 3): 1,
                 (6, 2): 1, (8, 2): 1, (6, 7): 1, (8, 7): 1,
                 (7, 2): 1, (7, 8): 1}

evalnum = 0
def get_center_value(row, col, randomlist = [], random = False):
    global center_values
    if not random:
        return center_values.get((row, col), -1)
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

# store position as (piece, row, col)
def get_piece_positions(board):
    positions = []
    for i in range(2, 13):
        if i == 2 or i == 12:
            for j in range(2, 8):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
        if i == 3 or i == 11:
            for j in range(2, 9):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
        if i == 4 or i == 10:
            for j in range(1, 9):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
        if i == 5 or i == 9:
            for j in range(1, 10):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
        if i == 6 or i == 8:
            for j in range(0, 10):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
        if i == 7:
            for j in range(0, 11):
                if board[i][j] == 2:
                    positions.append((2, i, j))
                if board[i][j] == 3:
                    positions.append((3, i, j))
    return positions

railing = {(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2), (3, 8), (4, 1), (4, 8),
           (5, 1), (5, 9), (6, 0), (6, 9), (7, 0), (7, 10), (8, 0), (8, 9), (9,1), (9, 9),
           (10, 1), (10, 8), (11, 2), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)}

def evaluate_pos1(positions, piece):
    global railing
    global evalnum
    evalnum += 1
    piececount = 0
    opp_piececount = 0
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    score = 0
    for marble in positions:
        if marble[0] == piece:
            if (marble[1], marble[2]) not in railing:
                piececount += 1
                score += 100 * get_center_value(marble[1], marble[2])
        elif marble[0] == opp_piece:
            if (marble[1], marble[2]) not in railing:
                opp_piececount += 1
                score -= 100 * get_center_value(marble[1], marble[2])
    score = score - (14 - piececount)*1000
    score = score + (14 - opp_piececount)*900
    return score


def Minimax(positions, depth, alpha, beta, piece, maximising, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = AI.is_terminal_node(positions)
    if depth == 0 or AI.is_terminal_node(positions):
        if is_terminal:
            if AI.winning_move(positions, piece):
                return None, 9999999999
            elif AI.winning_move(positions, opp_piece):
                return None, -9999999999
        else:
         #   return None, evaluate_posRandom(board, piece)
            return None, evaluate_pos1(positions, piece)
    if maximising:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(positions, piece, opp_piece)
        if move != -1:
            if move in valid_moves:
                valid_moves.remove(move)
        value = -math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
     #       b_copy = board.copy()
      #      b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
       #     new_score = Minimax(b_copy, depth - 1, alpha, beta, piece, False)[1]

            positions = AI.play_move_position(positions, move, piece, opp_piece)
            new_score = Minimax(positions, depth - 1, alpha, beta, piece, False)[1]
            positions = AI.undo_move_position(positions, move, piece, opp_piece)
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(positions, opp_piece, piece)
        value = math.inf
        move = random.choice(valid_moves)
        for move in valid_moves:
    #        b_copy = board.copy()
     #       b_copy, knock_off, row, col = AI.play_move(b_copy, move, opp_piece, piece)
      #      new_score = Minimax(b_copy, depth - 1,alpha, beta, piece, True)[1]

            positions = AI.play_move_position(positions, move, opp_piece, piece)
            new_score = Minimax(positions, depth - 1, alpha, beta, piece, True)[1]
            positions = AI.undo_move_position(positions, move, opp_piece, piece)
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value


# test functions
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def find_indexes(lst, elem):
    indexes = []
    for i in range(len(lst)):
        if lst[i] == elem:
            indexes.append(i)
    return indexes

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

def Minimax3(positions, depth, alpha, beta, piece, maximising, zobrist_table, move = -1):
    if piece == 2:
        opp_piece = 3
    elif piece == 3:
        opp_piece = 2
    is_terminal = AI.is_terminal_node(positions)
    if depth == 0 or AI.is_terminal_node(positions):
        if is_terminal:
            if AI.winning_move(positions, piece):
                return None, 9999999999
            elif AI.winning_move(positions, opp_piece):
                return None, -9999999999
        else:
            pos_score = evaluate_pos1(positions, piece)
            key = AI.generate_zobrist_key(positions)
            zobrist_table[key] = None, pos_score
        #    return None, evaluate_posRandom(board, piece)
            return None, pos_score
    if maximising:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(positions, piece, opp_piece)
        if move != -1:
            if move in valid_moves:
                valid_moves.remove(move)
        value = -math.inf
        for move in valid_moves:
     #       b_copy = board.copy()
      #      b_copy, knock_off, row, col = AI.play_move(b_copy, move, piece, opp_piece)
       #     new_score = Minimax3(b_copy, depth - 1, alpha, beta, piece, False)[1]
            positions = AI.play_move_position(positions, move, piece, opp_piece)
        # Look up the Zobrist key for the board state
            board_key = AI.generate_zobrist_key(positions)
            if board_key in zobrist_table:
                new_score = zobrist_table[board_key][1]
            new_score = Minimax3(positions, depth - 1, alpha, beta, piece, False, zobrist_table)[1]
            positions = AI.undo_move_position(positions, move, piece, opp_piece)
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_move, value

    else:
        valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(positions, opp_piece, piece)
        value = math.inf
        for move in valid_moves:
    #        b_copy = board.copy()
    #        b_copy, knock_off, row, col = AI.play_move(b_copy, move, opp_piece, piece)
     #       new_score = Minimax3(b_copy, depth - 1,alpha, beta, piece, True)[1]
            positions = AI.play_move_position(positions, move, opp_piece, piece)
             # Look up the Zobrist key for the board state
            board_key = AI.generate_zobrist_key(positions)
            if board_key in zobrist_table:
                new_score = zobrist_table[board_key][1]
            else:
                new_score = Minimax3(positions, depth - 1, alpha, beta, piece, True, zobrist_table)[1]
            positions = AI.undo_move_position(positions, move, opp_piece, piece)
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_move, value

level_times = []
level_times = move_pieces.get_level_times(level_times)
player_timer = 99999999999999999999
turn = 0
timer = 99999999999999999999
playing_game = False
in_menu = True
picked_pieces = False

# restart
restart_available = False
global save_board
shoving = False
highlighted = []
getting_pushed = []
run_the_loop = False
turn_swapped = False
CPU = True
AIvsAI = False
AI.get_all_moves(board, 3, 2)
movelist1 = []
movelist2 = []
#start_and_menu.title_card(screen, board)
start_and_menu.title_to_menu(screen)
just_broke_out = False
game_running = True
in_level_selector = False
in_level = False
start_time = pygame.time.get_ticks()
timer_backup = 9999999999
while game_running:
    while AIvsAI:
        if turn == 0:
            start1 = time.time()
            evalnum = 0
            positions = get_piece_positions(board)
            move, minimax_score = Minimax3(positions, 3, -math.inf, math.inf, 2, True, {})

         #   move, minimax_score = AI.iterative_deepener(5, board, -math.inf, math.inf, 2)
            print("black:")
            print("number of evals: " + str(evalnum))
            end1 = time.time()
            print(end1 - start1)
            print(minimax_score)
            movelist1.append(move)
            last2 = movelist1[-3:]
            if len(last2) == 3:
                if last2[0] == last2[2]:
                    move, minimax_score = Minimax(board, 3, -math.inf, math.inf, 2, True, move)
            board, knock_off, row, col = AI.play_move(board, move, 2, 3, knock_off)
            knocked_piece = 3
            if knock_off:
                knocked_off(board, row, col, knocked_piece)
                time_delay = False
                row = move[2][0]
                col = move[2][1]
                board[row][col] = starting_board[row][col]
                knock_off = False
            turn += 1
            turn = turn % 2
            if not in_level:
                board[0][9] = 300
            turn_swapped = True
            restart_available = True
            move_pieces.draw_board(board)
            pygame.display.update()

        if turn == 1:
            start2 = time.time()
            evalnum = 0
            positions = get_piece_positions(board)
            valid_moves, valid_shoves, valid_knocks = AI.get_all_moves(positions, 3, 2)
            move, minimax_score = Minimax3(positions, 3, -math.inf, math.inf, 3, True, {})
            print("white:")
            print("number of evals: " + str(evalnum))
            print(minimax_score)
            end2 = time.time()
            print(end2 - start2)
            board, knock_off, row, col = AI.play_move(board, move, 3, 2, knock_off)
            movelist2.append(move)
            last2 = movelist2[-3:]
            if len(last2) == 3:
                if last2[0] == last2[2]:
                    move, minimax_score = AI.Minimax(board, 3, -math.inf, math.inf, 3, True, move)

            board, knock_off, row, col = AI.play_move(board, move, 3, 2, knock_off)
            knocked_piece = 2
            if knock_off:
                knocked_off(board, row, col, knocked_piece)
                time_delay = False
                row = move[2][0]
                col = move[2][1]
                board[row][col] = starting_board[row][col]
                knock_off = False
            turn += 1
            turn = turn % 2
            if not in_level:
                board[0][9] = 200
            turn_swapped = True
            restart_available = True
            move_pieces.draw_board(board)
            pygame.display.update()


    while in_level_selector:
        highlighted = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    row, col = get_board_pos(posx, posy)
                    level = get_level_from_board(row, col)
                    if level != -1:
                        turn = 0
                        move_pieces.draw_board(boards[level])
                        playing_game = True
                        CPU = True
                        timer = level_times[level - 1]
                        board = copy.deepcopy(boards[level])
                        in_level_selector = False
                        in_level = True
                    if boards[0][row][col] == 999:
                        in_menu = True
                        playing_game = False
                        in_level_selector = False
                        board = move_pieces.create_board()
                        start_and_menu.levels_to_menu(screen)
                        board = move_pieces.create_board()
                        break
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        if in_level_selector:
            move_pieces.draw_board(boards[0])
            pygame.display.update()
   ############################################################MENU
    while in_menu:
        in_level = False
        highlighted = []
        if just_broke_out:
            start_and_menu.title_to_menu(screen)
            just_broke_out = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if pygame.mouse.get_pressed()[0]:
                posx = event.pos[0]
                posy = event.pos[1]
                # AI selected
                circlex2 = get_screen_pos(2, 7)[0]
                circley2 = get_screen_pos(2, 7)[1]
                if start_and_menu.is_point_inside_circle(posx, posy, circlex2, circley2, 60):
                    board[2][9] = 0
                    player_timer = 99999999999999999999
                    timer = -1
                    in_menu = False

                    # change these 3
          #          playing_game = True
           #         CPU = True
            #        AIvsAI = False

                    playing_game = False
                    CPU = False
                    AIvsAI = True

                    in_level_selector = False
                    move_pieces.draw_board(board)
                    pygame.display.update()
                 # 2 Player selected
                circlex1 = get_screen_pos(2, 2)[0]
                circley1 = get_screen_pos(2, 2)[1]
                if start_and_menu.is_point_inside_circle(posx, posy, circlex1, circley1, 60):
                    in_menu = False
                    CPU = False
                    playing_game = True
                    in_level_selector = False
                    move_pieces.draw_board(board)
                    pygame.display.update()
                    turn = 0
                    # Levels selected
                circlex3 = get_screen_pos(12, 2)[0]
                circley3 = get_screen_pos(12, 2)[1]
                if start_and_menu.is_point_inside_circle(posx, posy, circlex3, circley3, 60):
                    in_menu = False
                    in_level_selector = True
                    start_and_menu.menu_to_levels(screen)





    while playing_game:
        if turn_swapped:
            if knock_off == True:
                player_timer += 3
            turn_swapped = False
            knock_off = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                posx ,posy = pygame.mouse.get_pos()
                row, col = get_board_pos(posx, posy)
                # Back Button Pressed
                if board[row][col] == 999:
                    if in_level:
                        playing_game = False
                        in_level_selector = True
                        break
                    else:
                        turn = 0
                        in_menu = True
                        playing_game = False
                        # possibly remove this board creation, think obout creating seperate boards for ai and 2 player
                        board = move_pieces.create_board()
                        just_broke_out = True
                        player_timer = 9999999999
                        continue
                cx, cy = get_screen_pos(2, 9)
                # timer
                if start_and_menu.is_point_inside_circle(posx, posy, cx, cy, RADIUS + 10):
                    player_timer = start_and_menu.time_selection(screen)
                    timer_backup = player_timer
                    start_time = pygame.time.get_ticks()
                    if player_timer == -1 or player_timer == 0:
                        player_timer = 99999999999999999999
                if not in_level:
                    if restart_available:
                        # restart
                        if board[row][col] == 777:
                            save_board = copy.deepcopy(board)
                            board = move_pieces.create_board()
                            board[row][col] = 666
                            start_time = pygame.time.get_ticks()
                            if CPU:
                                board[2][9] = 0
                                move_pieces.draw_board(board)
                                pygame.display.update()
                                turn = 0
                    else:
                        if board[row][col] == 666:

                            board = save_board
                            if save_board[0][9] == 200:
                                turn = 0
                            if save_board[0][9] == 300:
                                turn = 1
                            board[row][col] = 777
                    if board[row][col] == 666:
                        restart_available = False

                if turn == 0:
                    if not in_level:
                        board[0][9] = 200
                    if not picked_pieces:
                        make_selection(board, row, col, highlighted, 2)
                    else:
                        this_turn = take_turn(board, row, col, highlighted, getting_pushed, 2)
                        if this_turn == 5:
                            knock_off = True
                            knocked_needs_reset = True
                            knocked_piece = 3
                            turn += 1
                            turn = turn % 2
                            if not in_level:
                                board[0][9] = 300
                                turn_swapped = True
                        elif this_turn == 4:
                            turn += 1
                            turn = turn % 2
                            if not in_level:
                                board[0][9] = 300
                            turn_swapped = True
                            start_time = pygame.time.get_ticks()
                        clean_board(board)

                        if not in_level:
                            board[2][0] = 777
                        for pos in highlighted:
                            unhighlight(board, pos[0], pos[1], 20)
                        highlighted = []
                        getting_pushed = []
                        picked_pieces = False
                        run_the_loop = False
                        restart_available = True

                if turn == 1 and run_the_loop:
                    if not CPU:
                        board[0][9] = 300
                        if not picked_pieces:
                            make_selection(board, row, col, highlighted, 3)
                        else:
                            this_turn = take_turn(board, row, col, highlighted, getting_pushed, 3)
                            if this_turn == 5:
                                knock_off = True
                                knocked_piece = 2
                                turn += 1
                                turn = turn % 2
                                board[0][9] = 200
                                turn_swapped = True
                            elif this_turn == 4:
                                turn += 1
                                turn = turn % 2
                                board[0][9] = 200
                                turn_swapped = True
                                start_time = pygame.time.get_ticks()
                            clean_board(board)
                            if not in_level:
                                board[2][0] = 777
                            for pos in highlighted:
                                unhighlight(board, pos[0], pos[1], 30)
                            highlighted = []
                            getting_pushed = []
                            picked_pieces = False
                            restart_available = True


                    if CPU:
                        depth = 3
                        if in_level:
                            depth = depthlist[level]
                        player_timer = 999999999999999999999
                        print(depth)
                        move, minimax_score = AI.Minimax(board, depth, -math.inf, math.inf, 3, True)
                      #  move, minimax_score = AI.iterative_deepener(5, board, -math.inf, math.inf, 3)
                        board, knock_off, row, col = AI.play_move(board, move, 3, 2, knock_off)
                        knocked_piece = 2
                        turn += 1
                        turn = turn % 2
                        if not in_level:
                            board[0][9] = 200
                        turn_swapped = True
                        restart_available = True

            if event.type == pygame.MOUSEBUTTONUP:
                if highlighted == []:
                    picked_pieces = False
                else:
                    if turn == 0:
                        opp_piece = 3
                    else:
                        opp_piece = 2
                    if len(highlighted) == 1:
                        move_pieces.show_moves1(board, highlighted)
                    if len(highlighted) == 2:
                        show_pushes2(board, highlighted, opp_piece)
                        move_pieces.show_slides2(board, highlighted)
                    if len(highlighted) == 3:
                        show_pushes3(board, highlighted, opp_piece)
                        move_pieces.show_slides3(board, highlighted)
                    picked_pieces = True

                print_board(board)

        move_pieces.draw_board(board)
        if in_level:
            adjust_board_for_lives_player(board, playerliveslist[level])
            adjust_board_for_lives_opp(board, oppliveslist[level])
            if level_times[level] != -1:
                player_timer = level_times[level]
                timer = player_timer
                if player_timer == -1:
                    player_timer = 99999999999999999999


        # End Game
        if in_level:
            if board[14][2] == 300:
                start_and_menu.beat_level(screen, board, oppliveslist[level], playerliveslist[level])
                in_level = False
                playing_game = False
                in_level_selector = True
                r, c = get_board_from_level(level)
                boards[0][r][c] = 6
            if board[0][7] == 200:
                start_and_menu.lost_level(screen, board, oppliveslist[level], playerliveslist[level])
                in_level = False
                playing_game = False
                in_level_selector = True
                r, c = get_board_from_level(level)
                boards[0][r][c] = 8

        # timer
        if player_timer < 500 and player_timer != 0:
            time_left = move_pieces.calculate_health(player_timer*1000, start_time)
            move_pieces.draw_rectangle(0, 0, time_left, 40, RED)
            if time_left == 0:
                start_time = pygame.time.get_ticks()
                turn += 1
                turn = turn % 2
                if not in_level:
                    if turn == 0:
                       board[0][9] = 200
                    if turn == 1:
                        board[0][9] = 300
                    player_timer = timer_backup
                    run_the_loop = False
                    clean_board(board)
                    for pos in highlighted:
                         unhighlight(board, pos[0], pos[1], 20)
                         unhighlight(board, pos[0], pos[1], 30)
                    highlighted = []
                    picked_pieces = False
        pygame.display.update()


        if knock_off:
            knocked_off(board, row, col, knocked_piece)
            time_delay = False
            board[row][col] = starting_board[row][col]
            knocked_needs_reset = False
            knock_off = False
            start_time = pygame.time.get_ticks()
        run_the_loop = True

