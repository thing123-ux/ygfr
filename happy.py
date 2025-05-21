import pygame, sys, random
pygame.init()
width = 300
height = 300
linewidth = 7
boardrows = 3
boardcols = 3
squaresize = 100
circleradius = 30
circlewidth=7
crosswidth=12
space=27
red = (255, 0 ,0)
bgcolor=(0,0,0)
linecolor=(255,255,255)
circlecolor=(0,0,255)
crosscolor=(255,0,0)

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("funni game")

board = [[0 for i in range(boardcols)] for j in range(boardrows)]

def drawlines():
    pygame.draw.line(screen, linecolor, (0, squaresize), (width, squaresize), linewidth)
    pygame.draw.line(screen, linecolor, (0, 2 * squaresize), (width, 2*squaresize), linewidth)

    pygame.draw.line(screen, linecolor, (squaresize, 0 ), (squaresize, height), linewidth)
    pygame.draw.line(screen, linecolor, (2 * squaresize, 0 ), (2 * squaresize, height), linewidth)
def drawfigures():
    for row in range(boardrows):
        for col in range (boardcols):
            if board[row][col] == 1:
                pygame.draw.line(screen,crosscolor, (col * squaresize + space, row * squaresize + squaresize - space) , (col * squaresize + squaresize-space, row * squaresize + space), crosswidth)
                pygame.draw.line(screen,crosscolor, (col * squaresize + space, row * squaresize + space) , (col * squaresize + squaresize-space, row * squaresize + squaresize -space), crosswidth)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, circlecolor, (int(col * squaresize + squaresize // 2), int(row * squaresize + squaresize //2)), circleradius, circlewidth )
def marksquare(row, col, player):
    board[row][col] = player
def availablesquare(row, col):
    if board[row][col] == 0:
        return True
screen.fill(bgcolor)
drawlines()
player = 1
gameover = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clickedrow = int(mouseY // squaresize)
            clickedcol = int(mouseX // squaresize)
            if availablesquare(clickedrow, clickedcol):
                marksquare(clickedrow,clickedcol,player)
                drawfigures()
                player = player % 2 + 1
    pygame.display.update()

