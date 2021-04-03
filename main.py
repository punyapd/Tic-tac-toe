import pygame
import sys
import numpy as np
WIDTH = 450
HEIGHT = 450
BG_COLOR = (28 , 170, 156)
LINE_COLOR = (255,255 , 255)
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // 3
CIRCLE_COLOR = ( 120 ,200 , 122)
CIRCLE_RADIUS = SQUARE_SIZE // 5
CROSS_COLOR = ( 200 , 200 , 200)
SPACE =  SQUARE_SIZE // 3
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tic tac toe")
board  = np.zeros((BOARD_ROWS , BOARD_COLS))
game_over = False

screen.fill(BG_COLOR)

def draw_lines():
    pygame.draw.line(screen , LINE_COLOR , (0 , SQUARE_SIZE) , (WIDTH ,SQUARE_SIZE) , 10)
    pygame.draw.line(screen , LINE_COLOR , (0,SQUARE_SIZE * 2) , (WIDTH , SQUARE_SIZE * 2) , 10)

    pygame.draw.line(screen , LINE_COLOR , (SQUARE_SIZE , 0) , (SQUARE_SIZE , WIDTH) , 10)
    pygame.draw.line(screen , LINE_COLOR , (SQUARE_SIZE * 2,0) , (SQUARE_SIZE * 2 , WIDTH) , 10)
def mark_square(row , col , player):
    board[row][col] = player
def available_square(row , col):
    return board[row][col] == 0
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
        return True
def draw_figure():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen , CIRCLE_COLOR , (int(col * SQUARE_SIZE +  SQUARE_SIZE // 2), int(row  * SQUARE_SIZE + SQUARE_SIZE // 2)) , CIRCLE_RADIUS , 10 )
            if board[row][col] == 2:
                pygame.draw.line(screen , CROSS_COLOR , (col * SQUARE_SIZE + SPACE  , row * SQUARE_SIZE + SQUARE_SIZE - SPACE) , (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE ) , 25)
                pygame.draw.line(screen , CROSS_COLOR , (col * SQUARE_SIZE + SPACE  , row * SQUARE_SIZE  + SPACE) , (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE ) , 25)
def check_win(player):
    # vertcal win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col ,player)
            return True
    #horizontal win check
    for row in range (BOARD_ROWS):
        if board[row][0] == player and board[row][1]== player and board[row][2] == player:
            draw_horizontal_winning_line(row , player)
            return True
    #asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # des diagonal win check 
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_des_diagonal(player)
        return True
    
def draw_vertical_winning_line(col , player):
    posx = col * SQUARE_SIZE +SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    
    pygame.draw.line(screen , color , (posx , 15) ,(posx , HEIGHT -15) , 15)
def draw_horizontal_winning_line(row , player):
    posy = row * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen ,color , (15, posy) ,(WIDTH- 15))
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen ,color , (15 , HEIGHT - 15) , (WIDTH - 15 , 15)  , 15)
def draw_des_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen , color , (15 , 15) , (WIDTH - 15 , HEIGHT - 15) , 15)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    game_over = False

draw_lines()


player = 1


#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            clicked_x = int(event.pos[1] // SQUARE_SIZE)
            clicked_y = int(event.pos[0] // SQUARE_SIZE)
           
            if available_square(clicked_x , clicked_y):
                if player == 1:
                    mark_square(clicked_x ,clicked_y , 1)
                    if  check_win(player):
                        game_over = True
                    player = 2 
                       
                elif player == 2:
                    mark_square(clicked_x , clicked_y , 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figure() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r :
                restart()
                game_over = False
                
    pygame.display.update()

