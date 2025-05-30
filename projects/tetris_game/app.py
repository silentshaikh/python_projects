import pygame
import random
 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [
    [
    '.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
 
 
class Piece(object):
    def __init__(self,x,y,shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0
        
 
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for _ in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    
    return grid

 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i ,line in enumerate(format):
        row = list(line)
        for j , col in enumerate(row):
            if col  == "0":
                positions.append((shape.x+j,shape.y+i))
    for i ,pos in enumerate(positions):
        positions[i] = (pos[0]-2,pos[1]-4)
    return positions
 
def valid_space(shape, grid):
    acceptedPos = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    acceptedPos = [j for sub in acceptedPos for j in sub]
    formated =  convert_shape_format(shape)
    for position in formated:
        if position not in acceptedPos:
            if position[1] > -1:
                return False
    return True


 
def check_lost(positions):
    for pos in positions:
        x,y = pos
        if y < 1:
            return True
    return False


 
def get_shape():
    return Piece(5,0,random.choice(shapes))


 
 
def draw_text_middle(surface,text, size, color):
    font = pygame.font.SysFont("comicsans",size,bold=True)
    label = font.render(text,1,color)

    surface.blit(label,(top_left_x+play_width/2-(label.get_width()/2),top_left_y+play_height/2- label.get_height()/2))
   
def draw_grid(surface,grid): #, row, col
   sx = top_left_x
   sy = top_left_y

   for i in range(len(grid)):
       pygame.draw.line(surface,(120,120,120),(sx,sy+i*block_size),(sx+play_width,sy+i*block_size))
       for j in range(len(grid[i])):
            pygame.draw.line(surface,(120,120,120),(sx+j*block_size,sy),(sx+j*block_size,sy+play_height))

           

 
def clear_rows(grid, locked):
   inc  = 0
   for i in range(len(grid)-1,-1,-1):
       row = grid[i]
       if (0,0,0) not in row:
           inc +=1
           ind = i
           for j in range(len(row)):
               try:
                   del locked[(j,i)]
               except:
                   continue
   if inc > 0:
    for key in sorted(list(locked),key=lambda x:x[1])[::-1]:
        x,y = key
        if y < ind:
            newKey = (x,y+inc)
            locked[newKey] = locked.pop(key)
   return inc

       
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans",30)
    label = font.render("Next Shape",1,(255,255,255))
    sx = top_left_x+play_width+50
    sy = top_left_y+play_height/2-100
    format= shape.shape[shape.rotation % len(shape.shape)]

    for i,line in enumerate(format):
        row = list(line)
        for j,col in enumerate(row):
            if col == "0":
                pygame.draw.rect(surface,shape.color,(sx+ j*block_size, sy + i * block_size,block_size,block_size),0)
    surface.blit(label,(sx+10,sy-30))


def updateScore(score):
    # with open("score.txt","r") as f:
    #    lines =  f.readline()
    #    scores = lines[0].strip()
    scores = maxScore()
    with open("score.txt","w") as f:
      if int(scores)>score:
          f.write(str(scores))
      else:
          f.write(str(score))


def maxScore():
    with open("score.txt","r") as f:
        lines =  f.readline()
        scores = lines.strip()
    return scores
    

 
def draw_window(surface,grid,score=0,lastScore=0):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont("comicsans",60)
    label = font.render("Tetris",1,(255,255,255))

    surface.blit(label,(top_left_x+play_width/2 - (label.get_width()/2),30))
 

    font = pygame.font.SysFont("comicsans",30)
    #current score
    label = font.render(f"Score : {score}",1,(255,255,255))
    sx = top_left_x+play_width+50
    sy = top_left_y+play_height/2-100

    surface.blit(label,(sx+20,sy+160))

    # last score
    label = font.render(f"High Score : {lastScore}",1,(255,255,255))
    sx = top_left_x-250
    sy = top_left_y+200

    surface.blit(label,(sx+20,sy+160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface,grid[i][j],(top_left_x+j*block_size,top_left_y + i*block_size,block_size,block_size),0)
    pygame.draw.rect(surface,(255,0,0), (top_left_x,top_left_y,play_width,play_height),4)
    # pygame.display.update()
    draw_grid(surface,grid)
    # pygame.display.update()
 
def main(win):
    lastScore = maxScore()
    lock_position = {}
    grid = create_grid(lock_position)
    changePiece = False
    run = True
    current_piece = get_shape()
    nextPeice = get_shape()
    clock = pygame.time.Clock()
    fallTime = 0
    fallSpeed = 0.27
    levelTime = 0
    score = 0
    while run:
        grid = create_grid(lock_position)
        fallTime += clock.get_rawtime() 
        levelTime += clock.get_rawtime()
        clock.tick()

        if levelTime/1000 > 5:
            levelTime = 0
            if levelTime > 0.12:
                levelTime -= 0.005

        if fallTime/1000 > fallSpeed:
            fallTime = 0
            current_piece.y +=1
            if not valid_space(current_piece,grid) and current_piece.y >0:
                current_piece.y -=1
                changePiece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =  False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -=1
                    if not valid_space(current_piece,grid):
                        current_piece.x +=1

                if event.key == pygame.K_RIGHT:
                    current_piece.x +=1
                    if not valid_space(current_piece,grid):
                        current_piece.x -=1
                if event.key == pygame.K_DOWN:
                    current_piece.y +=1
                    if not valid_space(current_piece,grid):
                        current_piece.y -=1
                
                if event.key == pygame.K_UP:
                    current_piece.rotation +=1
                    if not valid_space(current_piece,grid):
                        current_piece.rotation -= 1
        shapePos = convert_shape_format(current_piece)
        for i in range(len(shapePos)):
            x,y = shapePos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        
        if changePiece:
            for pos in shapePos:
                p = (pos[0],pos[1])
                lock_position[p] = current_piece.color
            current_piece = nextPeice
            nextPeice = get_shape()
            changePiece = False
            # clear_rows(grid,lock_position)
            score += clear_rows(grid,lock_position) * 10



        draw_window(win,grid,score,lastScore)
        draw_next_shape(nextPeice,win)
        pygame.display.update()

        if check_lost(lock_position):
            draw_text_middle(win,"You LosT !",80,(255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            updateScore(score)
    # pygame.display.quit()
 
def main_menu(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win,"Press ANy Key to PLay",60,(255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()



win  = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tetris")
main_menu(win)  