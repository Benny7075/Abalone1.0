import pygame
import math
import move_pieces
import time
import random
import copy
board = move_pieces.board
starting_board = copy.deepcopy(board)

railing = {(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2), (3, 8), (4, 1), (4, 8),
           (5, 1), (5, 9), (6, 0), (6, 9), (7, 0), (7, 10), (8, 0), (8, 9), (9,1), (9, 9),
           (10, 1), (10, 8), (11, 2), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)}


def knocked_off(board, row, col, piece):
    board[row][col] = 100*piece
    posx, posy = move_pieces.get_screen_pos(row, col)
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

def legal_sing_moves(emptys, marble, legal_moves):
    if marble[0] == 2:
        opp_piece = 3
    elif marble[0] == 3:
        opp_piece = 2
    for row in range(marble[1] - 2, marble[1] + 2):
        for col in range(marble[2] - 2, marble[2] + 2):
            if (row, col) in emptys and move_pieces.selectable2(row, col, [(marble[1], marble[2])]):
                legal_moves.append(((marble[1], marble[2]), (row, col)))


def selectable2_edited(row, col, highlighted):
    gotrow, gotcol = highlighted[0]
    if (col == gotcol + 1 and row == gotrow):
        return True
    elif move_pieces.slanted_row(row):
        if (row == gotrow - 1 and col == gotcol):
            return True
        if (row == gotrow + 1 and col == gotcol):
            return True
    else:
        if (row == gotrow - 1 and col == gotcol + 1):
            return True
        if (row == gotrow + 1 and col == gotcol + 1):
            return True
    return False


# now only looks in one direction
def selectable3_edited(row, col, highlighted):
    row1, col1 = highlighted[0]
    row2, col2 = highlighted[1]
    maxrow = max(row1, row2)
    minrow = min(row1, row2)
    maxcol = max(col1, col2)
    mincol = min(col1, col2)
    if row1 == row2:
        if row == row1 and (col == col2 + 1 or col == col1 + 1):
            return True
    elif move_pieces.slanted_row(row):
        if col1 == col2:
            if row == minrow - 1 and col == col1 - 1:
                return True
        if col2 == col1 + 1:
            if row2 < row1:
                if row == row2 - 1 and col == col2:
                    return True
        if col2 == col1 - 1:
            if row2 > row1:
                if row == row1 - 1 and col == col1:
                    return True
    else:
        if col1 == col2:
            if row == minrow - 1 and col == col1 + 1:
                return True
        if col2 == col1 + 1:
            if row2 > row1:
                if row == row1 - 1 and col == col1:
                    return True
        if col2 == col1 - 1:
            if row2 < row1:
                if row == row2 - 1 and col == col2:
                    return True
    return False

# edited to return boolean
def show_if_poss(emptys, row1, col1, row2, col2, row3, col3):
    slides = []
    if (row1, col1) in emptys and (row2, col2) in emptys:
        slides.append(((row1, col1), (row2, col2)))
    if (row3, col3) in emptys and (row2, col2) in emptys:
        slides.append(((row2, col2), (row3, col3)))
    return slides


def show_slides2(positions, emptys, highlighted):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    res = [1,7]
    highest_row = min(r1, r2)
    lowest_row = max(r1, r2)
    highest_col = max(c1, c2)
    lowest_col = min(c1, c2)
    possible_slides = []
    if r1 != r2:
        # lower slanted
        if move_pieces.slanted_row(lowest_row):
            # facing left
            if c1 == c2:
                # left side
                blues = show_if_poss(emptys ,highest_row, c1 - 1, lowest_row, c1 - 1, lowest_row + 1, c1)
                for slide in blues:
                    possible_slides.append(slide)
                # right side
                blues = show_if_poss(emptys , highest_row - 1, c1, highest_row, c1 + 1, lowest_row, c1 + 1)
                for slide in blues:
                    possible_slides.append(slide)
            # facing right
            if c1 != c2:
                # left side
                blues = show_if_poss(emptys , lowest_row, lowest_col - 1, highest_row, lowest_col, highest_row - 1, lowest_col)
                for slide in blues:
                    possible_slides.append(slide)
                # right side
                blues = show_if_poss(emptys , lowest_row + 1, highest_col, lowest_row, highest_col, highest_row, highest_col + 1)
                for slide in blues:
                    possible_slides.append(slide)
        else:
            # facing right
            if c1 == c2:
                # left side
                blues = show_if_poss(emptys , lowest_row, c1 - 1, highest_row, c1 - 1, highest_row - 1, c1)
                for slide in blues:
                    possible_slides.append(slide)
                # right side
                blues = show_if_poss(emptys , highest_row, c1 + 1, lowest_row, c1 + 1, lowest_row + 1, c1)
                for slide in blues:
                    possible_slides.append(slide)
            # facing left
            if c1 != c2:
                # left side
                blues = show_if_poss(emptys , lowest_row + 1, lowest_col, lowest_row, lowest_col, highest_row, lowest_col - 1)
                for slide in blues:
                    possible_slides.append(slide)
                # right side
                blues = show_if_poss(emptys , lowest_row, highest_col + 1, highest_row, highest_col, highest_row - 1, highest_col)
                for slide in blues:
                    possible_slides.append(slide)
    # flat
    if r1 == r2:
        if move_pieces.slanted_row(r1):
            # top
            blues = show_if_poss(emptys , r1 - 1, highest_col + 1, r1 - 1, highest_col, r1 - 1, lowest_col)
            for slide in blues:
                possible_slides.append(slide)
            # bottom
            blues = show_if_poss(emptys , r1 + 1, highest_col + 1, r1 + 1, highest_col, r1 + 1, lowest_col)
            for slide in blues:
                possible_slides.append(slide)
        else:
            # top
            blues = show_if_poss(emptys , r1 - 1, highest_col, r1 - 1, lowest_col, r1 - 1, lowest_col - 1)
            for slide in blues:
                possible_slides.append(slide)
            # bottom
            blues = show_if_poss(emptys , r1 + 1, highest_col, r1 + 1, lowest_col, r1 + 1, lowest_col - 1)
            for slide in blues:
                possible_slides.append(slide)
    return possible_slides

def get_empty_spots(positions):
    emptys = []
    for i in range(3, 12):
        if i == 3 or i == 11:
            for j in range(3, 8):
                if (2, i, j) not in positions and (3, i, j) not in positions:
                    emptys.append((i, j))
        if i == 4 or i == 10:
            for j in range(2, 8):
                if (2, i, j) not in positions and (3, i, j) not in positions:
                    emptys.append((i, j))
        if i == 5 or i == 9:
            for j in range(2, 9):
                if (2, i, j) not in positions and (3, i, j) not in positions:
                    emptys.append((i, j))
        if i == 6 or i == 8:
            for j in range(1, 9):
                if (2, i, j) not in positions and (3, i, j) not in positions:
                    emptys.append((i, j))
        if i == 7:
            for j in range(1, 10):
                if (2, i, j) not in positions and (3, i, j) not in positions:
                    emptys.append((i, j))
    return emptys


def not_possible(positions, emptys, row1, col1, row2, col2, row3, col3, row4, col4):
    slides3 = []
    if (row1, col1) in emptys and (row2, col2) in emptys and (row3, col3) in emptys:
        slides3.append(((row1, col1), (row2, col2), (row3, col3)))
    if (row4, col4) in emptys and (row2, col2) in emptys and (row3, col3) in emptys:
        slides3.append(((row2, col2), (row3, col3), (row4, col4)))
    return slides3


def show_slides3(positions, emptys, highlighted):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    r3, c3 = highlighted[2]
    moving_piece_rows = []
    moving_piece_cols = []
    for counter in highlighted:
        moving_piece_rows.append(counter[0])
        moving_piece_cols.append(counter[1])
    possible_slides3 = []
    rmax = max(r1, r2, r3)
    rmin = min(r1, r2, r3)
    cmax = max(c1, c2, c3)
    cmin = min(c1, c2, c3)
    first_pair = [highlighted[0], highlighted[1]]
    second_pair = [highlighted[1], highlighted[2]]
    # flat
    if rmax == rmin:
        if move_pieces.slanted_row(r1):
            # top
            slides3 = not_possible(positions, emptys, r1 - 1, cmin, r1 - 1, cmax - 1, r1 - 1, cmax, r1 - 1, cmax + 1)
            for slide in slides3:
                possible_slides3.append(slide)
            # bottom
            slides3 = not_possible(positions, emptys, r1 + 1, cmin, r1 + 1, cmax - 1, r1 + 1, cmax, r1 + 1, cmax + 1)
            for slide in slides3:
                possible_slides3.append(slide)
        else:
            # top
            slides3 = not_possible(positions, emptys, r1 - 1, cmin - 1, r1 - 1, cmin, r1 - 1, cmax - 1, r1 - 1, cmax)
            for slide in slides3:
                possible_slides3.append(slide)
            # bottom
            slides3 = not_possible(positions, emptys, r1 + 1, cmin - 1, r1 + 1, cmin, r1 + 1, cmax - 1, r1 + 1, cmax)
            for slide in slides3:
                possible_slides3.append(slide)
    else:
        for value in [r1, r2, r3]:
            if value != rmin and value != rmax:
                rmid = value
        index_max = moving_piece_rows.index(rmax)
        index_mid = moving_piece_rows.index(rmid)
        if move_pieces.slanted_row(rmax):
            # facing left
            if moving_piece_cols[index_max] == moving_piece_cols[index_mid]:
                # left side
                slides3 = not_possible(positions, emptys, rmin, cmin - 1, rmax - 1, cmin, rmax, cmin, rmax + 1, cmax)
                for slide in slides3:
                    possible_slides3.append(slide)
                # right side
                slides3 = not_possible(positions, emptys, rmax, cmax + 1, rmax - 1, cmax + 1, rmin, cmax, rmin - 1, cmax)
                for slide in slides3:
                    possible_slides3.append(slide)
            # facing right
            else:
                # left side
                slides3 = not_possible(positions, emptys, rmax, cmin - 1, rmin + 1, cmin, rmin, cmin, rmin - 1, cmax)
                for slide in slides3:
                    possible_slides3.append(slide)
                # right side
                slides3 = not_possible(positions, emptys, rmax + 1, cmax, rmax, cmax, rmin + 1, cmax + 1, rmin, cmax + 1)
                for slide in slides3:
                    possible_slides3.append(slide)
        else:
            # facing right
            if moving_piece_cols[index_max] == moving_piece_cols[index_mid]:
                # left side
                slides3 = not_possible(positions, emptys, rmin - 1, cmin, rmin, cmin, rmax - 1, cmin - 1, rmax, cmin - 1)
                for slide in slides3:
                    possible_slides3.append(slide)
                # right side
                slides3 = not_possible(positions, emptys, rmin, cmax + 1, rmax - 1, cmax, rmax, cmax, rmax + 1, cmin)
                for slide in slides3:
                    possible_slides3.append(slide)
            # facing left
            else:
                # left side
                slides3 = not_possible(positions, emptys, rmin, cmin - 1, rmax - 1, cmin - 1, rmax, cmin, rmax + 1, cmin)
                for slide in slides3:
                    possible_slides3.append(slide)
                # right side
                slides3 = not_possible(positions, emptys, rmax, cmax + 1, rmin + 1, cmax, rmin, cmax, rmin - 1, cmin)
                for slide in slides3:
                    possible_slides3.append(slide)
    return possible_slides3

def find_all_pairs(positions, piece):
    possible_pairs = []
    for marble in positions:
        if marble[0] == piece:
            for marble2 in positions:
                if marble2[0] == piece and selectable2_edited(marble2[1], marble2[2], [(marble[1], marble[2])]):
                    possible_pairs.append([(marble[1], marble[2]), (marble2[1], marble2[2])])
    return possible_pairs


def order_three(three):
    sorted_coords = sorted(three, key=lambda coord: (coord[0], coord[1]))
    if sorted_coords[0][0] == sorted_coords[1][0]:
        sorted_coords = sorted(sorted_coords, key=lambda coord: coord[1])
    return tuple(sorted_coords[2::-1] if sorted_coords[0][0] != sorted_coords[2][0] else sorted_coords)


def find_all_threes(positions, piece, pairs):
    possible_threes = []
    for marble in positions:
        for pair in pairs:
            if marble[0] == piece and selectable3_edited(marble[1], marble[2], pair):
                if (marble[1], marble[2]) not in pair:
                    three = [pair[0], pair[1], (marble[1], marble[2])]
                    three = order_three(three)
                    possible_threes.append(three)
    return possible_threes


def append_3push_moves(positions, emptys, threes, row, col, legal_moves, legal_shoves, legal_knocks, opp_piece):
    global railing
    for three in threes:
        first_pair = []
        second_pair = []
        r1, c1 = three[0]
        r2, c2 = three[1]
        r3, c3 = three[2]

        # on same row
        if r1 == r3:
            cmin = min(c1, c2, c3)
            cmax = max(c1, c2, c3)
            for marble in three:
                if marble[1] != cmax:
                    first_pair.append(marble)
                if marble[1] != cmin:
                    second_pair.append(marble)
        else:
            rmin = min(r1, r2, r3)
            rmax = max(r1, r2, r3)
            for marble in three:
                if marble[0] != rmin:
                    first_pair.append(marble)
                if marble[0] != rmax:
                    second_pair.append(marble)
        if (row, col) in emptys:
            if move_pieces.selectable3(row, col, first_pair):
                legal_moves.append((three[2], (row, col)))
            elif move_pieces.selectable3(row, col, second_pair):
                legal_moves.append((three[0], (row, col)))

        if (opp_piece, row, col) in positions and move_pieces.selectable3(row, col, first_pair):
            if abs(first_pair[0][0] - row) + abs(first_pair[0][1] - col) > abs(first_pair[1][0] - row) + abs(first_pair[1][1] - col):
                closest_marb = first_pair[1]
            else:
                closest_marb = first_pair[0]
            for marble in three:
                if marble not in first_pair:
                    furthest_marb = marble
            for r in range(row - 2, row + 2):
                for c in range(col - 2, col + 2):
                    if (r, c) in emptys or (r, c) in railing:
                        if move_pieces.selectable3(r, c, (closest_marb, (row, col))):
                            legal_moves.append((furthest_marb, (row, col), (r, c)))
                            legal_shoves.append((furthest_marb, (row, col), (r, c)))

                    #        print("three v 1: " + str((furthest_marb, (row, col), (r, c))))
                            if (r, c) in railing:
                                legal_knocks.append((furthest_marb, (row,col), (r, c)))

                    elif (opp_piece, r, c) in positions and move_pieces.selectable3(r, c, (closest_marb, (row, col))) and not (r == row and c == col):
                        for roww in range(r - 2, r + 2):
                            for coll in range(c - 2, c + 2):
                                if coll < 11:
                                    if (roww, coll) in emptys or (roww, coll) in railing:
                                        if move_pieces.selectable3(roww, coll, ((row, col), (r, c))):
                                            legal_moves.append((furthest_marb, (row, col), (roww, coll)))
                                            legal_shoves.append((furthest_marb, (row, col), (roww, coll)))

                                #            print("three v 2: " + str((furthest_marb, (row, col), (roww, coll))))

        elif (opp_piece, row, col) in positions and move_pieces.selectable3(row, col, second_pair):
            if abs(second_pair[0][0] - row) + abs(second_pair[0][1] - col) > abs(second_pair[1][0] - row) + abs(second_pair[1][1] - col):
                closest_marb = second_pair[1]
            else:
                closest_marb = second_pair[0]
            for marble in three:
                if marble not in second_pair:
                    furthest_marb = marble
            for r in range(row - 2, row + 2):
                for c in range(col - 2, col + 2):
                    if (r, c) in emptys or (r, c) in railing:
                        if move_pieces.selectable3(r, c, (closest_marb, (row, col))):
                            legal_moves.append((furthest_marb, (row, col), (r, c)))
                            legal_shoves.append((furthest_marb, (row, col), (r, c)))
                      #      print("three v 1: " + str((furthest_marb, (row, col), (r, c))))
                            if (r, c) in railing:
                                legal_knocks.append((furthest_marb, (row,col), (r, c)))

                    elif (opp_piece, r, c) in positions and move_pieces.selectable3(r, c, (closest_marb, (row, col))) and not (r == row and c == col):
                        for roww in range(r - 2, r + 2):
                            for coll in range(c - 2, c + 2):
                                if (roww, coll) in emptys or (roww, coll) in railing:
                                    if move_pieces.selectable3(roww, coll, ((row, col), (r, c))):
                                        legal_moves.append((furthest_marb, (row, col), (roww, coll)))
                                        legal_shoves.append((furthest_marb, (row, col), (roww, coll)))
                                   #     print("three v 2: " + str((furthest_marb, (row, col), (roww, coll))))
                                        if (r, c) in railing:
                                            legal_knocks.append((furthest_marb, (row, col), (roww, coll)))

def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

legal_moves = []
def get_all_moves(positions, piece, opp_piece):
    global railing
    emptys = get_empty_spots(positions)
    legal_moves = []
    legal_shoves = []
    legal_knocks = []
    pairs = find_all_pairs(positions, piece)
    threes = find_all_threes(positions, piece, pairs)

    for r in range(3, 12):
        for c in range(1, 10):
            # append all 3pushes
            append_3push_moves(positions, emptys, threes, r, c, legal_moves, legal_shoves, legal_knocks, opp_piece)


                # append all 2 pushes
            for pair in pairs:
                if (r, c) in emptys and move_pieces.selectable3(r, c, pair):
                    if abs(pair[0][0] - r) + abs(pair[0][1] - c) < abs(pair[1][0] - r) + abs(pair[1][1] - c):
                        legal_moves.append((pair[1], (r, c)))
                    else:
                        legal_moves.append((pair[0], (r, c)))
        # shove move recorded as (spot thats moved out of, spot where colour changed, spot pushed piece lands)
                elif (opp_piece, r, c) in positions and move_pieces.selectable3(r, c, pair):
                    if abs(pair[0][0] - r) + abs(pair[0][1] - c) < abs(pair[1][0] - r) + abs(pair[1][1] - c):
                        furthest_marb = pair[1]
                    else:
                        furthest_marb = pair[0]
                    for marble in pair:
                        if marble != furthest_marb:
                            closest_marble = marble
                    for row in range(r - 2, r + 2):
                        for col in range(c - 2, c + 2):
                            if (row, col) in emptys or (row, col) in railing:
                                if move_pieces.selectable3(row, col, (closest_marble, (r, c))):
                                 #   print((furthest_marb, (r,c), (row, col)))
                                    legal_moves.append((furthest_marb, (r,c), (row, col)))
                                    legal_shoves.append((furthest_marb, (r,c), (row, col)))
                                    if (row, col) in railing:
                                        legal_knocks.append((furthest_marb, (r,c), (row, col)))

    # append all single moves
    for marble in positions:
        if marble[0] == piece:
           legal_sing_moves(emptys, marble, legal_moves)

    for three in threes:
        slide_deses = show_slides3(positions, emptys, three)
        for slide in slide_deses:
            legal_moves.append((three, slide))
    for pair in pairs:
        slide_ends = show_slides2(positions, emptys, pair)
        for slide in slide_ends:
            legal_moves.append((pair, slide))

    return legal_moves, legal_shoves , legal_knocks

# just three pushes atm
def get_three_push_and_knocks(positions, piece, opp_piece):
    global railing
    emptys = get_empty_spots(positions)
    legal_moves = []
    legal_shoves = []
    legal_knocks = []
    pairs = find_all_pairs(positions, piece)
    threes = find_all_threes(positions, piece, pairs)
    for r in range(3, 12):
        for c in range(1, 10):
            append_3push_moves(positions, emptys, threes, r, c, legal_moves, legal_shoves, legal_knocks, opp_piece)
    return legal_moves, legal_shoves, legal_knocks


def play_move_position(positions, move, piece, opp_piece):
    # push moves
    if len(move) == 2:
        if isinstance(move[0][0], int):
            positions.remove((piece, move[0][0], move[0][1]))
            positions.append((piece, move[1][0], move[1][1]))
            return positions
        # slide moves
        else:
            for start in move[0]:
                positions.remove((piece, start[0], start[1]))
            for des in move[1]:
                positions.append((piece, des[0], des[1]))
            return positions
    if len(move) == 3:
        positions.remove((piece, move[0][0], move[0][1]))
        positions.append((piece, move[1][0], move[1][1]))
        positions.remove((opp_piece, move[1][0], move[1][1]))
        positions.append((opp_piece, move[2][0], move[2][1]))
        return positions


def undo_move_position(positions, move, piece, opp_piece):
    # push moves
    if len(move) == 2:
        if isinstance(move[0][0], int):
            positions.remove((piece, move[1][0], move[1][1]))
            positions.append((piece, move[0][0], move[0][1]))
            return positions
        # slide moves
        else:
            for start in move[1]:
                positions.remove((piece, start[0], start[1]))
            for des in move[0]:
                positions.append((piece, des[0], des[1]))
            return positions
    if len(move) == 3:
        positions.append((piece, move[0][0], move[0][1]))
        positions.remove((piece, move[1][0], move[1][1]))
        positions.append((opp_piece, move[1][0], move[1][1]))
        positions.remove((opp_piece, move[2][0], move[2][1]))
        return positions




def play_move(board, move, piece, opp_piece, knock_off = False):
    row = -1
    col = -1
    if len(move) == 2:
        if isinstance(move[0][0], int):
            board[move[0][0]][move[0][1]] = 1
            board[move[1][0]][move[1][1]] = int(piece)
        else:
            for counter in move[0]:
                board[counter[0]][counter[1]] = 1
            for des in move[1]:
                board[des[0]][des[1]] = piece
    if len(move) == 3:
        row = move[2][0]
        col = move[2][1]
        board[move[0][0]][move[0][1]] = 1
        board[move[1][0]][move[1][1]] = piece
        board[move[2][0]][move[2][1]] = opp_piece
        if starting_board[move[2][0]][move[2][1]] == 9:
            knock_off = True
    return board, knock_off, row, col


def undo_move(board, move, piece, opp_piece):
    if len(move) == 2:
        if isinstance(move[0][0], int):
            board[move[0][0]][move[0][1]] = int(piece)
            board[move[1][0]][move[1][1]] = int(1)
        else:
            for counter in move[0]:
                board[counter[0]][counter[1]] = piece
            for des in move[1]:
                board[des[0]][des[1]] = 1
    if len(move) == 3:
        row = move[2][0]
        col = move[2][1]
        board[move[0][0]][move[0][1]] = piece
        board[move[1][0]][move[1][1]] = opp_piece
        board[move[2][0]][move[2][1]] = 1
        if starting_board[move[2][0]][move[2][1]] == 9:
            board[move[2][0]][move[2][1]] = 9
    return board


def move_from_pos_difference(positions1, positions2, piece):
    if piece == 2:
        opp_piece = 3
    else:
        opp_piece = 2
    original = []
    des = []
    for pos in positions1:
        if pos not in positions2:
            original.append(pos)
    for pos in positions2:
        if pos not in positions1:
            des.append(pos)
    # simple push
    if len(original) == 1 and len(des) == 1:
        return ((original[0][1], original[0][2]), (des[0][1], des[0][2]))

    # slides
    if len(original) == 3:
        if original[0][0] == piece and original[1][0] == piece and original[2][0] == piece:
            return (((original[0][1], original[0][2]), (original[1][1], original[1][2]), (original[2][1], original[2][2])), ((des[0][1], des[0][2]), (des[1][1], des[1][2]), (des[2][1], des[2][2])))

    if len(original) == 2:
        if original[0][0] == piece and original[1][0] == piece:
            return (((original[0][1], original[0][2]), (original[1][1], original[1][2])), ((des[0][1], des[0][2]), (des[1][1], des[1][2])))

    # shove
    if len(original) == 2:
        for place in original:
            if (piece, place[1], place[2]) not in des:
                out = place
            else:
                swap = place
        for place in des:
            if (opp_piece, place[1], place[2]) not in original:
                end = place
        return ((out[1], out[2]), (swap[1], swap[2]), (end[1], end[2]))
    return None