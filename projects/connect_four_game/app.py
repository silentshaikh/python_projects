import pygame
import numpy as np
import math
import sys
blue =(0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
rowCount = 6
columnCount = 7
def create_board():
     board = np.zeros((6,7))
     return board

def dropPiece(board,row,col,piece):
    board[row][col] = piece


def isValidLocation(board,col):
    return board[5][col] == 0



def getNextOpenRow(board,col):
    for r in range(rowCount):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    for c in range(columnCount-3):
        for r in range(rowCount):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    

    for c in range(columnCount):
        for r in range(rowCount-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    
    for c in range(columnCount-3):
        for r in range(rowCount-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c] == piece:
                return True
    
    for c in range(columnCount-3):
        for r in range(3,rowCount):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c] == piece:
                return True

def drawBoard(board):
    for c in range(columnCount):
        for r in range(rowCount):
            pygame.draw.rect(screen,blue,(c*squareSize, r*squareSize+squareSize, squareSize,squareSize))
            # if board[r][c] == 0:
            pygame.draw.circle(screen,black,(int(c*squareSize+squareSize/2),int(r*squareSize+squareSize+squareSize/2)),radius)

    for c in range(columnCount):
        for r in range(rowCount):
            if board[r][c] == 1:
                pygame.draw.circle(screen,red,(int(c*squareSize+squareSize/2),height-int(r*squareSize+squareSize/2)),radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen,yellow,(int(c*squareSize+squareSize/2),height-int(r*squareSize+squareSize/2)),radius)
    pygame.display.update()
                

cretBoard = create_board()
printBoard(cretBoard)
gameOver = False
trun = 0

pygame.init()

squareSize = 100
width = columnCount * squareSize
height = (rowCount+1) * squareSize

size = (width,height)
radius = int(squareSize/2-5)
screen = pygame.display.set_mode(size)
drawBoard(cretBoard)
pygame.display.update()

myFont = pygame.font.SysFont("monospace",75)

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,squareSize))
            posx = event.pos[0]
            if trun == 0:
                pygame.draw.circle(screen,red,(posx,int(squareSize/2)),radius)
            else:
                pygame.draw.circle(screen,yellow,(posx,int(squareSize/2)),radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("")
            # continue
            print(event.pos)
            pygame.draw.rect(screen,black,(0,0,width,squareSize))
            if trun == 0:
                # col = int(input("Player 1 make your selection (0-6) :"))
                posx = event.pos[0]
                col = int(math.floor(posx/squareSize))


                if isValidLocation(cretBoard,col):
                    row = getNextOpenRow(cretBoard,col)
                    dropPiece(cretBoard,row,col,1)

                    if winning_move(cretBoard,1):
                        # print("Player 1 Wins !!! Congrats!!!")
                        label = myFont.render("Player 1 won",1,red)
                        screen.blit(label,(40,10))
                        gameOver = True


            else:
                # col = int(input("Player 2 make your selection (0-6) :"))
                posx = event.pos[0]
                col = int(math.floor(posx/squareSize))
                if isValidLocation(cretBoard,col):
                    row = getNextOpenRow(cretBoard,col)
                    dropPiece(cretBoard,row,col,2)

                    if winning_move(cretBoard,1):
                        # print("Player 2 Wins !!! Congrats!!!")
                        label = myFont.render("Player 1 won",1,yellow)
                        screen.blit(label,(40,10))
                        gameOver = True
    
        printBoard(cretBoard)
        drawBoard(cretBoard)
    
        trun += 1
        trun %= 2

        if gameOver:
            pygame.time.wait(3000)
        
