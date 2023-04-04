import math
import pygame
import numpy
import move_pieces
import copy


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
ORANGE = [255, 128, 0]
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
    board[0][0] = 2
    return board
board = create_board()

def create_blank_board():
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
    return board
blank_board = create_blank_board()

def slanted_row(row):
    if row == 2 or row == 4 or row == 6 or row == 8 or row == 0 or row == 10 or row == 12 or row == 14:
        return True
    return False


def get_screen_pos(row, col):
    posy = SQUARESIZE + 0.866*SQUARESIZE*row
    if move_pieces.slanted_row(row):
        posx = SQUARESIZE + col*SQUARESIZE
    else:
        posx = (SQUARESIZE/2) + SQUARESIZE*col
    return posx, posy

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

    for i in range(int(time)):
        # Move the circle
        pos = (circle[0] + i * speed_x, circle[1] + i * speed_y)
        if i >= 1:
            posgrey = (circle[0] + (i - 1) * speed_x, circle[1] + (i - 1) * speed_y)
            # Draw the circle
            pygame.draw.circle(screen, DDGREY, posgrey, 2*RADIUS)
            pygame.draw.circle(screen, BLACK, pos, 2*RADIUS)
            pygame.draw.circle(screen, LGREY, pos, RADIUS)
            pygame.display.update()
            # Wait for a short time to slow down the animation
            pygame.time.wait(10)
        posgrey = (circle[0] + (int(time) - 1) * speed_x, circle[1] + (int(time) - 1) * speed_y)
        pygame.draw.circle(screen, DDGREY, posgrey, 2*RADIUS)

def draw_line(screen, start, destination, velocity):

    # Calculate the distance to the destination
    dx = destination[0] - start[0]
    dy = destination[1] - start[1]
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5
    if distance == 0:
        return
    # Calculate the time it will take to reach the destination
    time = distance / velocity

    # Calculate the speed for each frame
    speed_x = dx / time
    speed_y = dy / time

    for i in range(int(time)):
        # Move the circle
        pos = (start[0] + i * speed_x, start[1] + i * speed_y)
        pygame.draw.circle(screen, WHITE, pos, 0.7 * RADIUS)
        pygame.time.wait(10)
        pygame.display.update()


def title_card(screen, board):
    screen.fill(DGREY)
    pygame.display.update()
    pygame.time.delay(500)

    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 0)[0] + 24, get_screen_pos(7, 0)[1]), 1.7 * RADIUS)
    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 10)[0] - 36, get_screen_pos(7, 10)[1]), 1.7 * RADIUS)
    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 2)[0] + 14.4, get_screen_pos(7, 2)[1]), 1.7*RADIUS)
    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 4)[0] - 5, get_screen_pos(7, 4)[1]), 1.7*RADIUS)
    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 6)[0] + 5.2, get_screen_pos(7, 6)[1]), 1.7*RADIUS)
    pygame.draw.circle(screen, BLACK, (get_screen_pos(7, 8)[0] - 14.4, get_screen_pos(7, 8)[1]), 1.7*RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 2)[0] + 14.4, get_screen_pos(7, 2)[1]), RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 4)[0] - 5, get_screen_pos(7, 4)[1]), RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 6)[0] + 5.2, get_screen_pos(7, 6)[1]), RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 8)[0] - 14.4, get_screen_pos(7, 8)[1]), RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 0)[0] + 24, get_screen_pos(7, 0)[1]), RADIUS)
    pygame.draw.circle(screen, DGREY, (get_screen_pos(7, 10)[0] - 36, get_screen_pos(7, 10)[1]), RADIUS)
    pygame.display.update()
    pygame.time.delay(300)
    draw_rectangle(118, 361, 40, 0.3 * RADIUS, DGREY, 90)
    draw_rectangle(108, 318, 100,  0.7 * RADIUS, BLACK, 90)
    draw_rectangle(83, 340, 64, 0.7 * RADIUS, BLACK, 132)
    draw_rectangle(83, 356, 64, 0.3 * RADIUS, DGREY, 132)
    pygame.display.update()
    pygame.time.delay(300)
    draw_rectangle(271, 318, 100, 0.7 * RADIUS, BLACK, 90)
    draw_rectangle(246, 340, 64, 0.7 * RADIUS, BLACK, 132)
    draw_rectangle(246, 356, 64, 0.3 * RADIUS, DGREY, 132)
    pygame.display.update()
    pygame.time.delay(300)
    draw_rectangle(393, 366, 64, 1.9 * RADIUS, DGREY, 90)
    draw_rectangle(369, 350, 40, 0.7 * RADIUS, BLACK, 90)
    draw_rectangle(417, 350, 40, 0.7 * RADIUS, BLACK, 90)
    pygame.display.update()
    pygame.time.delay(300)
    draw_rectangle(490, 342, 64,  1.3*RADIUS, DGREY, 160)
    draw_rectangle(480, 333, 35, 0.7 * RADIUS, BLACK, 20)
    pygame.display.update()
    draw_line(screen, (0, 400), (600, 400), 4)
    screen.fill(DGREY)


def shrink_4circles(screen, initial_radius, final_radius, shrink = True):
    radius = initial_radius
    # Loop until the circle is fully shrunk
    if shrink:
        while radius > final_radius:

            # Draw the circle
            screen.fill(DGREY)
            move_pieces.draw_board(blank_board)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 2), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 7), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 2), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 7), radius)

            pygame.display.update()

            # Slowly decrease the radius
            radius -= 2

            # Wait for a short time to slow down the animation
            pygame.time.wait(10)
    else:
        while radius < final_radius:
            # Draw the circle
            screen.fill(DGREY)
            move_pieces.draw_board(blank_board)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 2), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 7), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 2), radius)
            pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 7), radius)

            pygame.display.update()
            radius += 2

            # Wait for a short time to slow down the animation
            pygame.time.wait(10)

def put_icons_on(screen):
    # 2 player logo
    x1, y1 = get_screen_pos(2, 2)
    draw_rectangle(x1 - 15, y1, 20, 80, BLACK)
    draw_rectangle(x1 + 15, y1, 20, 80, WHITE)


    # AI logo
    x2, y2 = get_screen_pos(2, 7)
    draw_rectangle(x2, y2, 60, 80, DGREY)
    pygame.draw.circle(screen, RED, (x2, y2 - 18), 10)
    draw_rectangle(x2, y2 + 23, 17, 34, RED)


    # Levels logo
    x3, y3 = get_screen_pos(12, 2)
    for i in range(5):
        for j in range(5):
            if j == 0:
                pygame.draw.circle(screen, GREEN, (x3 - 30 + (15 * i), y3 - 30 + (j * 15)), 5)
            elif j == 1:
                pygame.draw.circle(screen, RED, (x3 - 22.5 + (15 * i), y3 - 30 + (j * 15)), 5)
                pygame.draw.circle(screen, GREEN, (x3 - 37.5 + (15 * i), y3 - 30 + (j * 15)), 5)
            elif j == 2:
                pygame.draw.circle(screen, RED, (x3 - 30 + (15 * i), y3 - 30 + (j * 15)), 5)
                pygame.draw.circle(screen, RED, (x3 - 45 + (15 * i), y3 - 30 + (j * 15)), 5)
                pygame.draw.circle(screen, RED, (x3 - 15 + (15 * i), y3 - 30 + (j * 15)), 5)
            elif j == 3:
                pygame.draw.circle(screen, RED, (x3 - 22.5 + (15 * i), y3 - 30 + (j * 15)), 5)
                pygame.draw.circle(screen, RED, (x3 - 37.5 + (15 * i), y3 - 30 + (j * 15)), 5)
            else:
                pygame.draw.circle(screen, RED, (x3 - 30 +(15*i), y3  - 30 + (j*15)), 5)

    # Sandbox mode
    x4, y4 = get_screen_pos(12, 7)
    draw_rectangle(x4 - 20, y4, 20, 80, WHITE)
    draw_rectangle(x4, y4 + 30, 60, 20, WHITE)
    pygame.display.update()



def title_to_menu(screen):
    shrink_4circles(screen, 300, 60)
    put_icons_on(screen)
    screen.fill(DGREY)

def menu_to_levels(screen):
    pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 2), 60)
    pygame.draw.circle(screen, DDGREY, get_screen_pos(2, 7), 60)
    pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 2), 60)
    pygame.draw.circle(screen, DDGREY, get_screen_pos(12, 7), 60)
  #  pygame.display.update()
   # pygame.time.delay(50)
    shrink_4circles(screen, 60, RADIUS - 2)

def levels_to_menu(screen):
    shrink_4circles(screen, RADIUS - 2, 60, False)
    put_icons_on(screen)
    pygame.display.update()

def is_point_inside_circle(x, y, cx, cy, radius):
    # Calculate the distance between the point and the center of the circle
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)

    # Check if the distance is less than or equal to the radius
    if distance <= radius:
        return True
    else:
        return False

def time_selection(screen):
    # Initialize the slider value
    slider_value = 0
    slider_pos = (50, height/2)
    dragging = False
    making_time_selection = True
    while making_time_selection:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.mouse.get_pressed()[0]:
                posx ,posy = pygame.mouse.get_pos()
                if abs(slider_pos[0] - posx) < 20 and abs(slider_pos[1] - posy) < 10:
                    dragging = True
                if is_point_inside_circle(posx, posy, 3*width/4, 500, 60):
                    return time
            elif event.type == pygame.MOUSEBUTTONUP:
                # Stop dragging the slider
                dragging = False
            if dragging:
                posx, _ = pygame.mouse.get_pos()
                posx = max(50, min(posx, 450))
                slider_pos = (posx, height/2)



        screen.fill(LRED)
        pygame.draw.circle(screen, BLACK, (width / 2, 200), 60)
        pygame.draw.circle(screen, LRED, (width / 2, 200), 50)
        pygame.draw.circle(screen, BLACK, (width / 2, 200), 10)
        draw_rectangle(width / 2, 180, 15, 40, BLACK)
        draw_rectangle(width / 2 + 15, 215, 40, 15, BLACK, 135)
        draw_rectangle(width / 2, height / 2, 400, 2, RED)
        # Draw the slider handle
        draw_rectangle(slider_pos[0], slider_pos[1], 40, 20, RED)
        time = 2 + slider_pos[0]//15
        if slider_pos[0] == 50:
            time = 0
            draw_rectangle(width / 2, 200, 130, 15, RED, 135)
            draw_rectangle(width / 2, 200, 130, 15, RED, 45)
        # Draw the slider value
        font = pygame.font.Font(None, 30)
        text = font.render(str(time), True, BLACK)
        screen.blit(text, (width/2, 500))

        # Go to game
        pygame.draw.circle(screen, GREEN, (3*width / 4, 500), 60)

        pygame.display.update()
    return playing_game, in_menu, just_broke_out, board

def beat_level(screen, board, opplives, playerlives):
    greenboard = copy.deepcopy(board)
    greenboard = blend_into_background(greenboard, 6, opplives, playerlives)
    move_pieces.draw_board(board)
    pygame.display.update()
    pygame.time.delay(400)
    recs_fill_screen(GREEN)
    move_pieces.draw_board(greenboard, False)
    pygame.display.update()
    pygame.time.delay(300)
    move_pieces.draw_board(board)
    pygame.display.update()
    pygame.time.delay(300)
    recs_fill_screen(GREEN)
    move_pieces.draw_board(greenboard, False)
    pygame.display.update()
    pygame.time.delay(2000)

def lost_level(screen, board, opplives, playerlives):
    redboard = copy.deepcopy(board)
    redboard = blend_into_background(redboard, 809, opplives, playerlives)
    move_pieces.draw_board(board)
    pygame.display.update()
    pygame.time.delay(400)
    recs_fill_screen(LRED)
    move_pieces.draw_board(redboard, False)
    pygame.display.update()
    pygame.time.delay(300)
    move_pieces.draw_board(board)
    pygame.display.update()
    pygame.time.delay(300)
    recs_fill_screen(LRED)
    move_pieces.draw_board(redboard, False)
    pygame.display.update()
    pygame.time.delay(2000)


def blend_into_background(board, colour, opplives, playerlives):
    for i in range(15):
        board[i][0] = colour
        board[i][10] = colour
        if i != 7:
            board[i][9] = colour
        if i != 5 and i != 6 and i != 7 and i != 8 and i != 9:
            board[i][1] = colour
            board[i][8] = colour
    for i in range(10):
        board[13][i] = colour
        board[1][i] = colour
    board[7][0] = 9
    board[7][10] = 9
    if colour == 6:
        colour = 607
    if playerlives == 1:
        for i in range(2, 7):
            board[0][i] = -1 + colour
    if playerlives == 2:
        for i in range(2, 6):
            board[0][i] = -1 + colour
    if playerlives == 3:
        for i in range(2, 5):
            board[0][i] = -1 + colour
    if playerlives == 4:
        for i in range(2, 4):
            board[0][i] = -1 + colour
    if playerlives == 5:
        board[0][2] = -1 + colour


    if opplives == 1:
        for i in range(3, 8):
            board[14][i] = -1 + colour
    if opplives == 2:
        for i in range(4, 8):
            board[14][i] = -1 + colour
    if opplives == 3:
        for i in range(5, 8):
            board[14][i] = -1 + colour
    if opplives == 4:
        for i in range(6, 8):
            board[14][i] = -1 + colour
    if opplives == 5:
        board[14][7] = -1 + colour
    return board

def recs_fill_screen(colour):
    draw_rectangle(width/2, 40, width, 200, colour)
    draw_rectangle(width/2, 650, width, 200, colour)
    draw_rectangle(0, 200, width, 200, colour, 60)
    draw_rectangle(width, 200, width, 200, colour, 120)
    draw_rectangle(0, 500, width, 200, colour, 120)
    draw_rectangle(width, 500, width, 200, colour, 60)