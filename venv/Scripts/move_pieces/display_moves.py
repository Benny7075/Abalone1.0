ROW_COUNT = 15
COLUMN_COUNT = 11

def slanted_row(row):
    if row == 2 or row == 4 or row == 6 or row == 8 or row == 0 or row == 10 or row == 12 or row == 14:
        return True
    return False

def drop_piece(board, row, col, piece):
    if board[row][col] == 1 or board[row][col] == 7:
        board[row][col] = piece


def selectable2(row, col, highlighted):
    gotrow, gotcol = highlighted[0]
    if (col == gotcol + 1 and row == gotrow) or (col == gotcol - 1 and row == gotrow):
        return True
    elif slanted_row(row):
        if (row == gotrow - 1 and col == gotcol - 1) or (row == gotrow - 1 and col == gotcol):
            return True
        if (row == gotrow + 1 and col == gotcol - 1) or (row == gotrow + 1 and col == gotcol):
            return True
    else:
        if (row == gotrow - 1 and col == gotcol + 1) or (row == gotrow - 1 and col == gotcol):
            return True
        if (row == gotrow + 1 and col == gotcol + 1) or (row == gotrow + 1 and col == gotcol):
            return True
    return False


def selectable3(row, col, highlighted):
    row1, col1 = highlighted[0]
    row2, col2 = highlighted[1]
    maxrow = max(row1, row2)
    minrow = min(row1, row2)
    maxcol = max(col1, col2)
    mincol = min(col1, col2)
    if row1 == row2:
        if row == row1 and (col == col2 + 1 or col == col2 - 1 or col == col1 + 1 or col == col1 - 1):
            return True
    elif slanted_row(row):
        if col1 == col2:
            if row == minrow - 1 and col == col1 - 1:
                return True
            if row == maxrow + 1 and col == col1 - 1:
                return True
        if col2 == col1 + 1:
            if row2 < row1:
                if row == row2 - 1 and col == col2:
                    return True
            if row2 > row1:
                if row == row2 + 1 and col == col2:
                    return True
        if col2 == col1 - 1:
            if row2 < row1:
                if row == row1 + 1 and col == col1:
                    return True
            if row2 > row1:
                if row == row1 - 1 and col == col1:
                    return True
    else:
        if col1 == col2:
            if row == minrow - 1 and col == col1 + 1:
                return True
            if row == maxrow + 1 and col == col1 + 1:
                return True
        if col2 == col1 + 1:
            if row2 < row1:
                if row == row1 + 1 and col == col1:
                    return True
            if row2 > row1:
                if row == row1 - 1 and col == col1:
                    return True
        if col2 == col1 - 1:
            if row2 < row1:
                if row == row2 - 1 and col == col2:
                    return True
            if row2 > row1:
                if row == row2 + 1 and col == col2:
                    return True
    return False


def show_moves1(board, highlighted):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1 and selectable2(r, c, highlighted):
                board[r][c] = 6


blues = []
def show_if_poss(board, row1, col1, row2, col2, row3, col3, piece, res, tellme = False):
    if not ((board[row1][col1] not in res and board[row3][col3] not in res) or board[row2][col2] not in res):
        blues.append((row1, col1))
        blues.append((row2, col2))
        blues.append((row3, col3))
        if not tellme:
            drop_piece(board, row1, col1, piece)
            drop_piece(board, row2, col2, piece)
            drop_piece(board, row3, col3, piece)
        if tellme:
            return True


def show_slides2(board, highlighted):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    res = [1,7]
    highest_row = min(r1, r2)
    lowest_row = max(r1, r2)
    highest_col = max(c1, c2)
    lowest_col = min(c1, c2)
    if r1 != r2:
        # lower slanted
        if slanted_row(lowest_row):
            # facing left
            if c1 == c2:
                # left side
                show_if_poss(board,highest_row, c1 - 1, lowest_row, c1 - 1, lowest_row + 1, c1, 7, res)
                # right side
                show_if_poss(board, highest_row - 1, c1, highest_row, c1 + 1, lowest_row, c1 + 1, 7, res)
            # facing right
            if c1 != c2:
                # left side
                show_if_poss(board, lowest_row, lowest_col - 1, highest_row, lowest_col, highest_row - 1, lowest_col, 7, res)
                # right side
                show_if_poss(board, lowest_row + 1, highest_col, lowest_row, highest_col, highest_row, highest_col + 1, 7, res)
        else:
            # facing right
            if c1 == c2:
                # left side
                show_if_poss(board, lowest_row, c1 - 1, highest_row, c1 - 1, highest_row - 1, c1, 7, res)
                # right side
                show_if_poss(board, highest_row, c1 + 1, lowest_row, c1 + 1, lowest_row + 1, c1, 7, res)
            # facing left
            if c1 != c2:
                # left side
                show_if_poss(board, lowest_row + 1, lowest_col, lowest_row, lowest_col, highest_row, lowest_col - 1, 7, res)
                # right side
                show_if_poss(board, lowest_row, highest_col + 1, highest_row, highest_col, highest_row - 1, highest_col, 7, res)
    # flat
    if r1 == r2:
        if slanted_row(r1):
            # top
            show_if_poss(board, r1 - 1, highest_col + 1, r1 - 1, highest_col, r1 - 1, lowest_col, 7, res)
            # bottom
            show_if_poss(board, r1 + 1, highest_col + 1, r1 + 1, highest_col, r1 + 1, lowest_col, 7, res)
        else:
            # top
            show_if_poss(board, r1 - 1, highest_col, r1 - 1, lowest_col, r1 - 1, lowest_col - 1, 7, res)
            # bottom
            show_if_poss(board, r1 + 1, highest_col, r1 + 1, lowest_col, r1 + 1, lowest_col - 1, 7, res)


def not_possible(board, row1, col1, row2, col2, row3, col3, row4, col4, res):
    if board[row1][col1] not in res or board[row2][col2] not in res or (board[row3][col3] not in res and board[row4][col4] not in res):
        drop_piece(board, row1, col1, 1)
        drop_piece(board, row2, col2, 1)
        drop_piece(board, row3, col3, 1)
        drop_piece(board, row4, col4, 1)


def show_slides3(board, highlighted):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    r3, c3 = highlighted[2]
    moving_piece_rows = []
    moving_piece_cols = []
    for counter in highlighted:
        moving_piece_rows.append(counter[0])
        moving_piece_cols.append(counter[1])
    res = [1, 7]
    rmax = max(r1, r2, r3)
    rmin = min(r1, r2, r3)
    cmax = max(c1, c2, c3)
    cmin = min(c1, c2, c3)
    first_pair = [highlighted[0], highlighted[1]]
    second_pair = [highlighted[1], highlighted[2]]
    show_slides2(board, first_pair)
    show_slides2(board, second_pair)
    # flat
    if rmax == rmin:
        if slanted_row(r1):
            # top
            not_possible(board, r1 - 1, cmin + 1, r1 - 1, cmax, r1 - 1, cmin, r1 - 1, cmax + 1, res)
            # bottom
            not_possible(board, r1 + 1, cmin + 1, r1 + 1, cmax, r1 + 1, cmin, r1 + 1, cmax + 1, res)
        else:
            # top
            not_possible(board, r1 - 1, cmin, r1 - 1, cmax - 1, r1 - 1, cmin - 1, r1 - 1, cmax, res)
            # bottom
            not_possible(board, r1 + 1, cmin, r1 + 1, cmax - 1, r1 + 1, cmin - 1, r1 + 1, cmax, res)
    else:
        for value in [r1, r2, r3]:
            if value != rmin and value != rmax:
                rmid = value
        index_max = moving_piece_rows.index(rmax)
        index_mid = moving_piece_rows.index(rmid)
        if slanted_row(rmax):
            # facing left
            if moving_piece_cols[index_max] == moving_piece_cols[index_mid]:
                # left side
                not_possible(board, rmax, cmin, rmax - 1, cmin, rmin, cmin - 1, rmax + 1, cmax, res)
                # right side
                not_possible(board, rmax - 1, cmax + 1, rmin, cmax, rmax, cmax + 1, rmin - 1, cmax, res)
            # facing right
            else:
                # left side
                not_possible(board, rmin + 1, cmin, rmin, cmin, rmax, cmin - 1, rmin - 1, cmax, res)
                # right side
                not_possible(board, rmin + 1, cmax + 1, rmax, cmax, rmax + 1, cmax, rmin, cmax + 1, res)
        else:
            # facing right
            if moving_piece_cols[index_max] == moving_piece_cols[index_mid]:
                # left side
                not_possible(board, rmax - 1, cmin - 1, rmin, cmin, rmin - 1, cmin, rmax, cmin - 1, res)
                # right side
                not_possible(board, rmax, cmax, rmax - 1, cmax, rmin, cmax + 1, rmax + 1, cmin, res)
            # facing left
            else:
                # left side
                not_possible(board, rmin + 1, cmin - 1, rmax, cmin, rmax + 1, cmin, rmin, cmin - 1, res)
                # right side
                not_possible(board, rmin, cmax, rmin + 1, cmax, rmax, cmax + 1, rmin - 1, cmin, res)