# list of 61 boards....
import pygame
import numpy

ROW_COUNT = 15
COLUMN_COUNT = 11

def get_level_times(level_times):
    for _ in range(62):
        level_times.append(-1)
    level_times[1] = -1
    return level_times

def get_opp_lives(liveslist):
    for i in range(61):
        liveslist.append(6)
    liveslist[1] = 6
    return liveslist

def get_player_lives(liveslist):
    for i in range(61):
        liveslist.append(6)
    liveslist[1] = 1
    return liveslist

def create_boardLevels():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 8

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 8
        board[8][i] = 8
    for i in range(2, 9):
        board[5][i] = 8
        board[9][i] = 8
    for i in range(2, 8):
        board[4][i] = 8
        board[10][i] = 8
    for i in range(3, 8):
        board[3][i] = 8
        board[11][i] = 8
    board[0][0] = 999
    return board

def create_board1():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    board[3][3] = 3
    board[3][7] = 3
    board[4][7] = 3
    board[10][7] = 3
    board[8][1] = 3
    board[8][2] = 3
    board[4][3] = 2
    board[3][4] = 2
    board[4][4] = 2
    board[4][6] = 2
    board[3][6] = 2
    board[10][6] = 2
    board[8][5] = 2
    board[8][4] = 2
    board[8][3] = 2
    board[10][5] = 2
    board[5][8] = 2
    return board

def create_board2():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 2
        board[8][i] = 3
    for i in range(2, 9):
        board[5][i] = 3
        board[9][i] = 2
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board3():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board4():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board5():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board6():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board7():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 9
    return board

def create_board8():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board9():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board10():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board11():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board12():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board13():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board14():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board15():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board16():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board17():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board18():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board19():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board20():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board21():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board22():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board23():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board24():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board25():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board26():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board27():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board28():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board29():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board30():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board31():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board32():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board33():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    board[2][0]  = 777
    return board

def create_board34():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board35():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board36():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board37():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board38():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board39():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board40():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board41():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board42():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board43():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board44():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board45():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board46():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board47():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board48():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board49():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board50():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board51():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board52():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board53():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board54():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board55():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board56():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board57():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board58():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board59():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board60():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

def create_board61():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    # rectangle pieces
    board[7][0] = 9
    board[7][10] = 9
    board[3][2] = 9
    board[3][8] = 9
    board[4][1] = 9
    board[4][8] = 9
    board[5][1] = 9
    board[5][9] = 9
    board[6][0] = 9
    board[6][9] = 9
    board[8][0] = 9
    board[8][9] = 9
    board[9][1] = 9
    board[9][9] = 9
    board[10][1] = 9
    board[10][8] = 9
    board[11][2] = 9
    board[11][8] = 9

    board[0][2] = 60
    board[0][3] = 60
    board[0][4] = 60
    board[0][5] = 60
    board[0][6] = 60
    board[0][7] = 60
    board[14][2] = 50
    board[14][3] = 50
    board[14][4] = 50
    board[14][5] = 50
    board[14][6] = 50
    board[14][7] = 50
    for i in range(1, 10):
        board[7][i] = 1

    for i in range(2, 8):
        board[2][i] = 9
        board[12][i] = 9

    for i in range(1, 9):
        board[6][i] = 1
        board[8][i] = 1
    for i in range(2, 9):
        board[5][i] = 1
        board[9][i] = 1
    for i in range(2, 8):
        board[4][i] = 1
        board[10][i] = 1
    for i in range(3, 8):
        board[3][i] = 1
        board[11][i] = 1
    board[0][0] = 999
    return board

