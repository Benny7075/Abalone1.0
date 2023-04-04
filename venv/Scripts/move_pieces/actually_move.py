
def slanted_row(row):
    if row == 2 or row == 4 or row == 6 or row == 8 or row == 0 or row == 10 or row == 12 or row == 14:
        return True
    return False


def push_piece(board, row, col, highlighted, piece):
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
    board[row][col] = piece
    if row < highest_row:
        board[lowest_row, moving_piece_cols[index_low]] = 1
    if row > lowest_row:
        board[highest_row, moving_piece_cols[index_high]] = 1
    if len(highlighted) != 1:
        if highest_row == lowest_row:
            if col < lowest_col:
                board[row, highest_col] = 1
            if col > highest_col:
                board[row, lowest_col] = 1
    else:
        board[highlighted[0][0]][highlighted[0][1]] = 1


def perform_slide2(board,row, col, r1, c1, rmid, cmid, r2, c2, piece):
    if col == c1 and row == r1:
        board[r1][c1] = piece
        board[rmid][cmid] = piece
        return True
    elif col == c2 and row == r2:
        board[rmid][cmid] = piece
        board[r2][c2] = piece
        return True
    elif col == cmid and row == rmid:
        if board[r1][c1] != 7:
            board[rmid][cmid] = piece
            board[r2][c2] = piece
            return True
        if board[r2][c2] != 7:
            board[rmid][cmid] = piece
            board[r1][c1] = piece
            return True

def slide_piece2(board, row, col, highlighted, piece):
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    cmin = min(c1, c2)
    cmax = max(c1, c2)
    rmin = min(r1, r2)
    rmax = max(r1, r2)
    # flat
    if r2 == r1:
        if slanted_row(r1):
            # bottom
            if row > r1:
                 if perform_slide2(board, row, col, r1 + 1, cmin, r1 + 1, cmax, r1 + 1, cmax + 1, piece):
                     return True
            # top
            if row < r1:
                if perform_slide2(board, row, col, r1 - 1, cmin, r1 - 1, cmax, r1 - 1, cmax + 1, piece):
                    return True
        else:
            # bottom
            if row > r1:
                if perform_slide2(board, row, col, r1 + 1, cmin - 1, r1 + 1, cmin, r1 + 1, cmax, piece):
                    return True
            # top
            if row < r1:
                if perform_slide2(board, row, col, r1 - 1, cmin - 1, r1 - 1, cmin, r1 - 1, cmax, piece):
                    return True
    elif slanted_row(rmax):
        # facing left
        if c1 == c2:
            # left side
            if perform_slide2(board, row, col, rmin, c1 - 1, rmax, c1 - 1, rmax + 1, c1, piece):
                return True
            # right side
            if perform_slide2(board, row, col, rmax, c1 + 1, rmin, c1 + 1, rmin - 1, c1, piece):
                return True
        # facing right
        else:
            # left side
            if perform_slide2(board, row, col, rmax, cmin - 1, rmin, cmin, rmin - 1, cmin, piece):
                return True
            # right side
            if perform_slide2(board, row, col, rmax + 1, cmax, rmax, cmax, rmin, cmax + 1, piece):
                return True
    else:
        # facing right
        if c1 == c2:
            # left side
            if perform_slide2(board, row, col, rmin - 1, c1, rmin, c1 - 1, rmax, c1 - 1, piece):
                return True
            # right side
            if perform_slide2(board, row, col, rmin, c1 + 1, rmax, c1 + 1, rmax + 1, c1, piece):
                return True
        # facing left
        else:
            # left side
            if perform_slide2(board, row, col, rmax + 1, cmin, rmax, cmin, rmin, cmin - 1, piece):
                return True
            # right side
            if perform_slide2(board, row, col, rmax, cmax + 1, rmin, cmax, rmin - 1, cmax, piece):
                return True


def perform_slide3(board,row, col, rmin, cmin, rmid1, cmid1, rmid2, cmid2, rmax, cmax, piece):
    res = [1, 7]
    if board[rmin][cmin] not in res:
        if (col == cmax and row == rmax) or (col == cmid2 and row == rmid2) or (col == cmid1 and row == rmid1):
            board[rmid1][cmid1] = piece
            board[rmid2][cmid2] = piece
            board[rmax][cmax] = piece
            return True

    if board[rmax][cmax] not in res:
        if (col == cmin and row == rmin) or (col == cmid2 and row == rmid2) or (col == cmid1 and row == rmid1):
            board[rmid1][cmid1] = piece
            board[rmid2][cmid2] = piece
            board[rmin][cmin] = piece
            return True

    if (col == cmin and row == rmin) or (col == cmid1 and row == rmid1):
        board[rmin][cmin] = piece
        board[rmid1][cmid1] = piece
        board[rmid2][cmid2] = piece
        return True

    elif (col == cmax and row == rmax) or (col == cmid2 and row == rmid2):
        board[rmid1][cmid1] = piece
        board[rmid2][cmid2] = piece
        board[rmax][cmax] = piece
        return True

def slide_piece3(board, row, col, highlighted, piece):
    moving_piece_rows = []
    moving_piece_cols = []
    for counter in highlighted:
        moving_piece_rows.append(counter[0])
        moving_piece_cols.append(counter[1])
    r1, c1 = highlighted[0]
    r2, c2 = highlighted[1]
    r3, c3 = highlighted[2]
    cmin = min(c1, c2, c3)
    cmax = max(c1, c2, c3)
    rmin = min(r1, r2, r3)
    rmax = max(r1, r2, r3)
    # flat
    if rmax == rmin:
        if slanted_row(r1):
            # top
            if perform_slide3(board, row, col, r1 - 1, cmin, r1 - 1, cmin + 1, r1 - 1, cmax, r1 - 1, cmax + 1, piece):
                return True
            # bottom
            if perform_slide3(board, row, col, r1 + 1, cmin, r1 + 1, cmin + 1, r1 + 1, cmax, r1 + 1, cmax + 1, piece):
                return True
        else:
            # top
            if perform_slide3(board, row, col, r1 - 1, cmin - 1, r1 - 1, cmin, r1 - 1, cmin + 1, r1 - 1, cmax, piece):
                return True
            # bottom
            if perform_slide3(board, row, col, r1 + 1, cmin - 1, r1 + 1, cmin, r1 + 1, cmin + 1, r1 + 1, cmax, piece):
                return True
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
                if perform_slide3(board, row, col, rmax + 1, cmax, rmax, cmin, rmax - 1, cmin, rmin, cmin - 1, piece):
                    return True
                # right side
                if perform_slide3(board, row, col, rmax, cmax + 1, rmin + 1, cmax + 1, rmin, cmax, rmin - 1, cmax, piece):
                    return True
            # facing right
            else:
                # left side
                if perform_slide3(board, row, col, rmax, cmin - 1, rmax - 1 , cmin, rmin, cmin, rmin - 1, cmax, piece):
                    return True
                # right side
                if perform_slide3(board, row, col, rmax + 1, cmax, rmax, cmax, rmin + 1, cmax + 1, rmin, cmax + 1, piece):
                    return True
        else:
            # facing right
            if moving_piece_cols[index_max] == moving_piece_cols[index_mid]:
                # left side
                if perform_slide3(board, row, col, rmax, cmin - 1, rmin + 1, cmin - 1, rmin, cmin, rmin - 1, cmin, piece):
                    return True
                # right side
                if perform_slide3(board, row, col, rmax + 1, cmin, rmax, cmax, rmax - 1, cmax, rmin, cmax + 1, piece):
                    return True
            # facing left
            else:
                # left side
                if perform_slide3(board, row, col, rmax + 1, cmin, rmax, cmin, rmax - 1, cmin - 1, rmin, cmin - 1, piece):
                    return True
                # right side
                if perform_slide3(board, row, col, rmax, cmax + 1, rmin + 1, cmax, rmin, cmax, rmin - 1, cmin, piece):
                    return True

def shove_piece(board, row, col, highlighted, piece):
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
    if row < highest_row:
        board[lowest_row, moving_piece_cols[index_low]] = 1
    if row > lowest_row:
        board[highest_row, moving_piece_cols[index_high]] = 1
    if highest_row == lowest_row:
        if col < lowest_col:
            board[row, highest_col] = 1
        if col > highest_col:
            board[row, lowest_col] = 1