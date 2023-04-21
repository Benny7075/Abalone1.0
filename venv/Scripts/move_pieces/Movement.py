import math
import pygame
import numpy
import copy

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
LGREY = [120,120,120]
DGREY = [50,50,50]
DDGREY = [30,30,30]
YELLOW = [195,190,54]
GREEN = [116,209,106]
BLUE = [106, 164, 209]
LBLUE = [188, 212, 230]
RED = [255,50,50]
LRED = [255, 110, 100]
ROW_COUNT = 15
COLUMN_COUNT = 11

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


def create_board():
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
        for i in range(4,7):
            board[5][i] = 3
            board[9][i] = 2

    for i in range(2, 8):
        board[4][i] = 3
        board[10][i] = 2
    for i in range(3, 8):
        board[3][i] = 3
        board[11][i] = 2
    board[0][9] = 200
    board[0][0] = 999
    board[2][9] = 888
    board[2][0]  = 777
    return board

board = create_board()

def draw_rectangle(x, y, width, height, color, rotation=0):
    """Draw a rectangle, centered at x, y.

    Arguments:
      x (int/float):
        The x coordinate of the center of the shape.
      y (int/float):
        The y coordinate of the center of the shape.
      width (int/float):
        The width of the rectangle.
      height (int/float):
        The height of the rectangle.
      color (str):
        Name of the fill color, in HTML format.
    """
    points = []

    # The distance from the center of the rectangle to
    # one of the corners is the same for each corner.
    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    # Get the angle to one of the corners with respect
    # to the x-axis.
    angle = math.atan2(height / 2, width / 2)

    # Transform that angle to reach each corner of the rectangle.
    angles = [angle, -angle + math.pi, angle + math.pi, -angle]

    # Convert rotation from degrees to radians.
    rot_radians = (math.pi / 180) * rotation

    # Calculate the coordinates of each point.
    for angle in angles:
        y_offset = -1 * radius * math.sin(angle + rot_radians)
        x_offset = radius * math.cos(angle + rot_radians)
        points.append((x + x_offset, y + y_offset))

    pygame.draw.polygon(screen, color, points)


def draw_board(board, fillScreen = True):
    if fillScreen:
        screen.fill(DGREY)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            ROW_POS = int(0.866*r*SQUARESIZE + SQUARESIZE)
            if slanted_row(r):
                PUSH_COL_POS = int(c*SQUARESIZE + SQUARESIZE)
                if board[r][c] == 0:
                    pygame.draw.circle(screen, DGREY, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 1:
                    pygame.draw.circle(screen, DGREY, (PUSH_COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, LGREY, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 2:
                    pygame.draw.circle(screen, DGREY, (PUSH_COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, BLACK,(PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == -2:
                    pygame.draw.circle(screen, BLACK,(PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == -3:
                    pygame.draw.circle(screen, WHITE, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 3:
                    pygame.draw.circle(screen, DGREY, (PUSH_COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, WHITE, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 9:
                    pygame.draw.circle(screen, DDGREY, (PUSH_COL_POS, ROW_POS), TROTH_RAD)
                if board[r][c] == 20:
                    pygame.draw.circle(screen, YELLOW, (PUSH_COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, BLACK, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 30:
                    pygame.draw.circle(screen, RED, (PUSH_COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, WHITE, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 6:
                    pygame.draw.circle(screen, GREEN, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 7:
                    pygame.draw.circle(screen, BLUE, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 808:
                    pygame.draw.circle(screen, LRED, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 999:
                    pygame.draw.circle(screen, LRED, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 777:
                    pygame.draw.circle(screen, RED, (PUSH_COL_POS, ROW_POS), RADIUS + 10)
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 10, 40, LRED, 90)
                if board[r][c] == 666:
                    pygame.draw.circle(screen, BLUE, (PUSH_COL_POS, ROW_POS), RADIUS + 10)
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 10, 40, LBLUE, 135)
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 10, 40, LBLUE, 45)
                if board[r][c] == 888:
                    pygame.draw.circle(screen, BLUE, (PUSH_COL_POS, ROW_POS), RADIUS + 10)
                    draw_rectangle(PUSH_COL_POS, ROW_POS - 10, 5, 20, LBLUE)
                    draw_rectangle(PUSH_COL_POS + 7.5, ROW_POS + 7.5, 5, 15, LBLUE, 45)
                    pygame.draw.circle(screen, LBLUE, (PUSH_COL_POS, ROW_POS), 4)

            else:
                COL_POS = int(c*SQUARESIZE + SQUARESIZE/2)
                if board[r][c] == 0:
                    pygame.draw.circle(screen, DGREY, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 1:
                    pygame.draw.circle(screen, DGREY, (COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, LGREY, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 2:
                    pygame.draw.circle(screen, DGREY, (COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, BLACK, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == -2:
                    pygame.draw.circle(screen, BLACK,(COL_POS, ROW_POS), RADIUS)
                if board[r][c] == -3:
                    pygame.draw.circle(screen, WHITE, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 3:
                    pygame.draw.circle(screen, DGREY, (COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, WHITE, (COL_POS, ROW_POS),RADIUS)
                if board[r][c] == 809:
                    pygame.draw.circle(screen, LRED, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 9:
                    pygame.draw.circle(screen, DDGREY, (COL_POS, ROW_POS), TROTH_RAD)
                if board[r][c] == 20:
                    pygame.draw.circle(screen, YELLOW, (COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, BLACK, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 30:
                    pygame.draw.circle(screen, RED, (COL_POS, ROW_POS), HIGH_RAD)
                    pygame.draw.circle(screen, WHITE, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 6:
                    pygame.draw.circle(screen, GREEN, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 7:
                    pygame.draw.circle(screen, BLUE, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 888:
                    pygame.draw.circle(screen, BLUE, (COL_POS, ROW_POS), RADIUS + 50)
    draw_rectangle(264, 48, 240, 2 * TROTH_RAD, DDGREY)
    draw_rectangle(264, get_screen_pos(5, 13)[0] - 0.866 * 24 + 1, 240, 2 * TROTH_RAD, DDGREY)
    draw_rectangle(264, 131, 240, 2 * TROTH_RAD, DDGREY)
    draw_rectangle(264, 545, 240, 2 * TROTH_RAD, DDGREY)
    draw_rectangle(84, 234.5, 240, 2 * TROTH_RAD, DDGREY, 60)
    draw_rectangle(444, 234, 240, 2 * TROTH_RAD, DDGREY, 120)
    draw_rectangle(444, 440, 240, 2 * TROTH_RAD, DDGREY, 60)
    draw_rectangle(84, 440, 240, 2 * TROTH_RAD, DDGREY, 120)


    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            ROW_POS = int(0.866 * r * SQUARESIZE + SQUARESIZE)
            if slanted_row(r):
                PUSH_COL_POS = int(c * SQUARESIZE + SQUARESIZE)
                if board[r][c] == 101:
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, DGREY)
                if board[r][c] == 808:
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, LRED)
                if board[r][c] == 606:
                    draw_rectangle(PUSH_COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, GREEN)
            else:
                COL_POS = int(c * SQUARESIZE + SQUARESIZE / 2)
                if board[r][c] == 808:
                    draw_rectangle(COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, LRED)
                if board[r][c] == 606:
                    draw_rectangle(COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, GREEN)
                if board[r][c] == 101:
                    draw_rectangle(COL_POS, ROW_POS, 5*RADIUS, 2*RADIUS + 10, DGREY)


    draw_rectangle(384, 96, 96, 2 * TROTH_RAD, DDGREY, 90)
    draw_rectangle(144, get_screen_pos(5, 12)[0] - 0.866 * 24 + 1, 96, 2 * TROTH_RAD, DDGREY, 90)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            ROW_POS = int(0.866 * r * SQUARESIZE + SQUARESIZE)
            if slanted_row(r):
                PUSH_COL_POS = int(c * SQUARESIZE + SQUARESIZE)
                if board[r][c] == 50:
                    pygame.draw.circle(screen, DDGREY, (PUSH_COL_POS, ROW_POS), TROTH_RAD)
                    pygame.draw.circle(screen, YELLOW, (PUSH_COL_POS, ROW_POS), SMALL_RAD)
                    pygame.draw.circle(screen, BLACK, (PUSH_COL_POS, ROW_POS), DOT)
                if board[r][c] == 60:
                    pygame.draw.circle(screen, DDGREY, (PUSH_COL_POS, ROW_POS), TROTH_RAD)
                    pygame.draw.circle(screen, RED, (PUSH_COL_POS, ROW_POS), SMALL_RAD)
                    pygame.draw.circle(screen, WHITE, (PUSH_COL_POS, ROW_POS), DOT)
                if board[r][c] == 8:
                    pygame.draw.circle(screen, LRED, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 200:
                    pygame.draw.circle(screen, BLACK, (PUSH_COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 300:
                    pygame.draw.circle(screen, WHITE, (PUSH_COL_POS, ROW_POS), RADIUS)
            else:
                COL_POS = int(c * SQUARESIZE + SQUARESIZE / 2)
                if board[r][c] == 50:
                    pygame.draw.circle(screen, DDGREY, (COL_POS, ROW_POS), TROTH_RAD)
                    pygame.draw.circle(screen, YELLOW, (COL_POS, ROW_POS), SMALL_RAD)
                    pygame.draw.circle(screen, BLACK, (COL_POS, ROW_POS), DOT)
                if board[r][c] == 60:
                    pygame.draw.circle(screen, DDGREY, (COL_POS, ROW_POS), TROTH_RAD)
                    pygame.draw.circle(screen, RED, (COL_POS, ROW_POS), SMALL_RAD)
                    pygame.draw.circle(screen, WHITE, (COL_POS, ROW_POS), DOT)
                if board[r][c] == 8:
                    pygame.draw.circle(screen, LRED, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 200:
                    pygame.draw.circle(screen, BLACK, (COL_POS, ROW_POS), RADIUS)
                if board[r][c] == 300:
                    pygame.draw.circle(screen, WHITE, (COL_POS, ROW_POS), RADIUS)



def slanted_row(row):
    if row == 2 or row == 4 or row == 6 or row == 8 or row == 0 or row == 10 or row == 12 or row == 14:
        return True
    return False

def get_screen_pos(row, col):
    posy = SQUARESIZE + 0.866*SQUARESIZE*row
    if slanted_row(row):
        posx = SQUARESIZE + col*SQUARESIZE
    else:
        posx = (SQUARESIZE/2) + SQUARESIZE*col
    return posx, posy

def get_board_pos(posx, posy):
    r = int(math.floor((posy - (0.5*SQUARESIZE))/(0.866*SQUARESIZE)))
    if slanted_row(r):
        COL_POS = int(math.floor((posx + (SQUARESIZE/2))/ SQUARESIZE)) - 1
    else:
        COL_POS = int(math.floor(posx / SQUARESIZE))
    return r, COL_POS

def move_circle(screen, circle, destination, velocity, piece):
    if piece == 2:
        colour = BLACK
    elif piece == 3:
        colour = WHITE

    # Calculate the distance to the destination
    dx = destination[0] - circle[0]
    dy = destination[1] - circle[1]
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5
    if distance == 0:
        return
    # Calculate the time it will take to reach the destination
    time = distance / velocity

    # Calculate the speed for each frame
    speed_x = dx / time
    speed_y = dy / time

    # in these cases we draw scoreboard
    if get_board_pos(circle[0], circle[1])[0] == 0:
        for i in range(int(time)):
            for j in range(get_board_pos(destination[0], destination[1])[1] , 8):
                if board[0][j] == 60:
                    pygame.draw.circle(screen, DDGREY, get_screen_pos(0, j), TROTH_RAD)
                    pygame.draw.circle(screen, RED, get_screen_pos(0, j), SMALL_RAD)
                    pygame.draw.circle(screen, WHITE, get_screen_pos(0, j), DOT)
            if i >= 1:
                posgrey = (circle[0] + (i - 1) * speed_x, circle[1] + (i - 1) * speed_y)
                pygame.draw.circle(screen, DDGREY, posgrey, RADIUS)

            pos = (circle[0] + i * speed_x, circle[1] + i * speed_y)
            pygame.draw.circle(screen, colour, pos, RADIUS)
            pygame.display.update()
            pygame.time.wait(10)
    elif get_board_pos(circle[0], circle[1])[0] == 14:
        for i in range(int(time)):
            for j in range(2, get_board_pos(destination[0], destination[1])[1]):
                if board[14][j] == 50:
                    pygame.draw.circle(screen, DDGREY, get_screen_pos(14, j), TROTH_RAD)
                    pygame.draw.circle(screen, YELLOW, get_screen_pos(14, j), SMALL_RAD)
                    pygame.draw.circle(screen, BLACK, get_screen_pos(14, j), DOT)
            if i >= 1:
                posgrey = (circle[0] + (i - 1) * speed_x, circle[1] + (i - 1) * speed_y)
                pygame.draw.circle(screen, DDGREY, posgrey, RADIUS)

            pos = (circle[0] + i * speed_x, circle[1] + i * speed_y)
            pygame.draw.circle(screen, colour, pos, RADIUS)
            pygame.display.update()
            pygame.time.wait(10)
    else:
        for i in range(int(time)):
            # Move the circle
            pos = (circle[0] + i * speed_x, circle[1] + i * speed_y)
            if i >= 1:
                posgrey = (circle[0] + (i - 1) * speed_x, circle[1] + (i - 1) * speed_y)
                # Draw the circle
                pygame.draw.circle(screen, DDGREY, posgrey, RADIUS)
            pygame.draw.circle(screen, colour, pos, RADIUS)
            pygame.display.update()
            # Wait for a short time to slow down the animation
            pygame.time.wait(10)
        posgrey = (circle[0] + (int(time) - 1) * speed_x, circle[1] + (int(time) - 1) * speed_y)
        pygame.draw.circle(screen, DDGREY, posgrey, RADIUS)

def move_round_edge(screen, circle_center, piece):
    row, col = get_board_pos(circle_center[0],circle_center[1])
    if piece == 2:
        if col <= 4:
            if row == 12:
                move_circle(screen, circle_center, get_screen_pos(12, 2), 3, piece)
                circle_center = get_screen_pos(12, 2)
            if row > 7:
                move_circle(screen, circle_center, get_screen_pos(7, 0), 3, piece)
                circle_center = get_screen_pos(7, 0)
            if row > 2:
                move_circle(screen, circle_center, get_screen_pos(2, 2), 3, piece)
                circle_center = get_screen_pos(2, 2)
            move_circle(screen, circle_center, get_screen_pos(2, 7), 3, piece)
        if col > 4:
            if row == 12:
                move_circle(screen, circle_center, get_screen_pos(12, 7), 3, piece)
                circle_center = get_screen_pos(12, 7)
            if row > 7:
                move_circle(screen, circle_center, get_screen_pos(7, 10), 3, piece)
                circle_center = get_screen_pos(7, 10)
            move_circle(screen, circle_center, get_screen_pos(2, 7), 3, piece)
    if piece == 3:
        if col <= 4:
            if row == 2:
                move_circle(screen, circle_center, get_screen_pos(2, 2), 3, piece)
                circle_center = get_screen_pos(2, 2)
            if row < 7:
                move_circle(screen, circle_center, get_screen_pos(7, 0), 3, piece)
                circle_center = get_screen_pos(7, 0)
            move_circle(screen, circle_center, get_screen_pos(12, 2), 3, piece)

        if col > 4:
            if row == 2:
                move_circle(screen, circle_center, get_screen_pos(2, 7), 3, piece)
                circle_center = get_screen_pos(2, 7)
            if row < 7:
                move_circle(screen, circle_center, get_screen_pos(7, 10), 3, piece)
                circle_center = get_screen_pos(7, 10)
            if row < 12:
                move_circle(screen, circle_center, get_screen_pos(12, 7), 3, piece)
                circle_center = get_screen_pos(12, 7)
            move_circle(screen, circle_center, get_screen_pos(12, 2), 3, piece)

def see_us_home(screen, circle_center, destination, piece):
    if piece == 2:
        move_circle(screen, circle_center, get_screen_pos(0,7), 3, piece)
        move_circle(screen, get_screen_pos(0,7) , destination, 3, piece)
    if piece == 3:
        move_circle(screen, circle_center, get_screen_pos(14,2), 3, piece)
        move_circle(screen, get_screen_pos(14,2) , destination, 3, piece)


railing = {(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2), (3, 8), (4, 1), (4, 8),
           (5, 1), (5, 9), (6, 0), (6, 9), (7, 0), (7, 10), (8, 0), (8, 9), (9,1), (9, 9),
           (10, 1), (10, 8), (11, 2), (11, 8), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7)}

def move_piece(screen, board, highlighted, is_shove, shove2, is_slide, start, destination, velocity, piece):
    if piece == 2:
        opp_piece = 3
        opp_colour = WHITE
        colour = BLACK
    elif piece == 3:
        opp_piece = 2
        colour = WHITE
        opp_colour = BLACK

    if not is_slide:
        # Calculate the distance to the destination
        dx = destination[0] - start[0]
        dy = destination[1] - start[1]
        if len(highlighted) == 2:
            dx = dx/2
            dy = dy/2
        if len(highlighted) == 3:
            dx = dx/3
            dy = dy/3
        distance = ((dx ** 2) + (dy ** 2)) ** 0.5
        if distance == 0:
            return
        # Calculate the time it will take to reach the destination
        time = distance / velocity

        # Calculate the speed for each frame
        speed_x = dx / time
        speed_y = dy / time
        if len(highlighted) == 1:
            # keep board right
            x, y = get_board_pos(destination[0], destination[1])
            ani_board = copy.deepcopy(board)
            ani_board[x][y] = 1
            for i in range(int(time)):
                # Move the circle
                pos = (start[0] + i * speed_x, start[1] + i * speed_y)
                draw_board(ani_board)
                pygame.draw.circle(screen, colour, pos, RADIUS)
                pygame.display.update()
                # Wait for a short time to slow down the animation
                pygame.time.wait(10)


        if len(highlighted) == 2:
            # keep board right
            x, y = get_board_pos(destination[0], destination[1])
            ani_board = copy.deepcopy(board)
            ani_board[x][y] = 1
            ani_board[highlighted[0][0]][highlighted[0][1]] = 1
            ani_board[highlighted[1][0]][highlighted[1][1]] = 1
            if is_shove:
                x1, y1 = get_board_pos(destination[0] + time * speed_x, destination[1] + time * speed_y)
                if (x1, y1) in railing:
                    ani_board[x1][y1] = 9
                else:
                    ani_board[x1][y1] = 1

            for i in range(int(time)):
                # Move the circle
                s1, s2 = get_screen_pos(highlighted[0][0], highlighted[0][1])
                t1, t2 = get_screen_pos(highlighted[1][0], highlighted[1][1])
                draw_board(ani_board)
                if is_shove:
                    pos3 = (destination[0] + i * speed_x, destination[1] + i * speed_y)
                    pygame.draw.circle(screen, opp_colour, pos3, RADIUS)
                pos1 = (s1 + i * speed_x, s2 + i * speed_y)
                pos2 = (t1 + i * speed_x, t2 + i * speed_y)
                pygame.draw.circle(screen, colour, pos1, RADIUS)
                pygame.draw.circle(screen, colour, pos2, RADIUS)
                pygame.display.update()
                # Wait for a short time to slow down the animation
                pygame.time.wait(10)

        if len(highlighted) == 3:
            x1, y1 = get_board_pos(destination[0] +  time * speed_x, destination[1] + time * speed_y)
            # keep board right
            x, y = get_board_pos(destination[0], destination[1])
            ani_board = copy.deepcopy(board)
            ani_board[x][y] = 1
            ani_board[highlighted[0][0]][highlighted[0][1]] = 1
            ani_board[highlighted[1][0]][highlighted[1][1]] = 1
            ani_board[highlighted[2][0]][highlighted[2][1]] = 1
            if is_shove:
                if (x1, y1) in railing:
                    ani_board[x1][y1] = 9
                else:
                    ani_board[x1][y1] = 1
            if shove2:
                x2, y2 = get_board_pos(destination[0] + 2*time * speed_x, destination[1] + 2*time * speed_y)
                if (x2, y2) in railing:
                    ani_board[x2][y2] = 9
                else:
                    ani_board[x2][y2] = 1
            for i in range(int(time)):
                # Move the circles
                s1, s2 = get_screen_pos(highlighted[0][0], highlighted[0][1])
                t1, t2 = get_screen_pos(highlighted[1][0], highlighted[1][1])
                u1, u2 = get_screen_pos(highlighted[2][0], highlighted[2][1])
                draw_board(ani_board)
                if is_shove:
                    pos4 = (destination[0] + i * speed_x, destination[1] + i * speed_y)
                    pygame.draw.circle(screen, opp_colour, pos4, RADIUS)
                if shove2:
                    pos5 = ((destination[0] + time * speed_x) + i * speed_x, (destination[1] + time * speed_y) + i * speed_y)
                    #pos5 = (destination[0] + 2*i * speed_x, destination[1] + 2*i * speed_y)
                    pygame.draw.circle(screen, opp_colour, pos5, RADIUS)
                pos1 = (s1 + i * speed_x, s2 + i * speed_y)
                pos2 = (t1 + i * speed_x, t2 + i * speed_y)
                pos3 = (u1 + i * speed_x, u2 + i * speed_y)
                pygame.draw.circle(screen, colour, pos1, RADIUS)
                pygame.draw.circle(screen, colour, pos2, RADIUS)
                pygame.draw.circle(screen, colour, pos3, RADIUS)
                pygame.display.update()
                # Wait for a short time to slow down the animation
                pygame.time.wait(10)

    if is_slide:
        # Calculate the distance to the destination
        desx, desy = get_screen_pos(destination[0][0], destination[0][1])
        startx, starty = get_screen_pos(start[0][0], start[0][1])
        dx = desx - startx
        dy = desy - starty
        distance = ((dx ** 2) + (dy ** 2)) ** 0.5
        if distance == 0:
            return
        # Calculate the time it will take to reach the destination
        time = distance / velocity

        # Calculate the speed for each frame
        speed_x = dx / time
        speed_y = dy / time

        if len(highlighted) == 2:
            # keep board right
            ani_board = copy.deepcopy(board)
            ani_board[destination[0][0]][destination[0][1]] = 1
            ani_board[destination[1][0]][destination[1][1]] = 1
            for i in range(int(time)):
                s1, s2 = get_screen_pos(start[1][0], start[1][1])
                pos1 = (startx + i * speed_x, starty + i * speed_y)
                pos2 = (s1 + i * speed_x, s2 + i * speed_y)
                draw_board(ani_board)
                pygame.draw.circle(screen, colour, pos1, RADIUS)
                pygame.draw.circle(screen, colour, pos2, RADIUS)
                pygame.display.update()
                # Wait for a short time to slow down the animation
                pygame.time.wait(10)
        elif len(highlighted) == 3:
            # keep board right
            ani_board = copy.deepcopy(board)
            ani_board[destination[0][0]][destination[0][1]] = 1
            ani_board[destination[1][0]][destination[1][1]] = 1
            ani_board[destination[2][0]][destination[2][1]] = 1
            for i in range(int(time)):
                s1, s2 = get_screen_pos(start[1][0], start[1][1])
                s_1, s_2 = get_screen_pos(start[2][0], start[2][1])
                pos1 = (startx + i * speed_x, starty + i * speed_y)
                pos2 = (s1 + i * speed_x, s2 + i * speed_y)
                pos3 = (s_1 + i * speed_x, s_2 + i * speed_y)
                draw_board(ani_board)
                pygame.draw.circle(screen, colour, pos1, RADIUS)
                pygame.draw.circle(screen, colour, pos2, RADIUS)
                pygame.draw.circle(screen, colour, pos3, RADIUS)
                pygame.display.update()
                # Wait for a short time to slow down the animation
                pygame.time.wait(10)


# takes in board after move has been played
def animate_move(board, move, highlghted, velocity, piece):
    if len(move) == 2 and not isinstance(move[0][0], int):
        move_piece(screen, board, highlghted, False, False, True, move[0], move[1], velocity, piece)
    else:
        if len(move) == 3:
            if is_it_shove2(move):
                move_piece(screen, board, highlghted, True, True, False, get_screen_pos(move[0][0], move[0][1]), get_screen_pos(move[1][0], move[1][1]), velocity, piece)
            else:
                move_piece(screen, board, highlghted, True, False, False, get_screen_pos(move[0][0], move[0][1]), get_screen_pos(move[1][0], move[1][1]), velocity, piece)

        else:
            move_piece(screen, board, highlghted, False, False, False, get_screen_pos(move[0][0], move[0][1]), get_screen_pos(move[1][0], move[1][1]), velocity, piece)


def is_it_shove2(move):
    swap = move[1]
    end = move[2]
    if abs(swap[0] - end[0]) >= 2 or abs(swap[1] - end[1]) >= 2:
        return True
    return False

def get_highlighted_from_AI(move):
    if len(move) == 2 and not isinstance(move[0][0], int):
        return move[0]


def calculate_health(time_to_zero, start_time):
    # Set up the health bar
    health_width = width*2
    health_height = 20
    health_x = 100
    health_y = 50
    health = health_width

    # Calculate the time elapsed since the start of the game
    time_elapsed = pygame.time.get_ticks() - start_time

    # Calculate the health percentage based on the time elapsed
    health_percent = (time_to_zero - time_elapsed) / time_to_zero
    if health_percent < 0:
        health_percent = 0

    # Calculate the current health based on the health percentage
    health = health_width * health_percent

    return health
