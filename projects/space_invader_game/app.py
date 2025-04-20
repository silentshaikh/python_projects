import pygame
import random,math
from pygame import mixer
pygame.init()

bgImg = pygame.image.load("background.png")

mixer.music.load("background.wav")
mixer.music.play(-1)

gameScren = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerXChange = 0

enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyXChange.append(4)
    enemyYChange.append(40)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = 10
bulletState = "ready"

score = 0
font = pygame.font.SysFont("comicsans",50)
textX =10
textY = 10

overFont = pygame.font.SysFont("comicsans",80)

def gameOver(x,y):
    overValue = font.render(f"GAME OVER",True,(255,0,255))
    gameScren.blit(overValue,(x,y))
def gameScore():
    scoreValue = overFont.render(f"Score : {score}",True,(255,255,255))
    gameScren.blit(scoreValue,(200,250))
def player(x,y):
    gameScren.blit(playerImg,(x,y))

def enemy(x,y,i):
    gameScren.blit(enemyImg[i],(x,y))

def fine_bullet(x,y):
    global bulletState
    bulletState = "fire"
    gameScren.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,buletX,buletY):
    distance = math.sqrt((math.pow(enemyX-buletX,2)) + (math.pow(enemyY-buletY,2)))
    if distance< 27:
        return True
    else:
        return False



running = True
while running:
    gameScren.fill((0,0,0))
    gameScren.blit(bgImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left arrow is pressed")
                playerXChange = -5
            
            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed")
                playerXChange = 5
            
            if event.key == pygame.K_SPACE:
                # print("Right arrow is pressed")
                if bulletState == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fine_bullet(bulletX,bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Key Stokes has been released")
                playerXChange = 0

    playerX += playerXChange
    if playerX <=0 :
        playerX = 0
    elif playerX >=736:
        playerX = 736

    for  i in range(numOfEnemies):
        if enemyY[i] > 200:
            for j in range(numOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            break

        enemyX[i] += enemyXChange[i]
        if enemyX[i] <=0 :
            enemyXChange[i] = 4
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -4
            enemyY[i] += enemyYChange[i]
        collision= isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"
            score +=1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState == "fire":
        fine_bullet(bulletX,bulletY)
        bulletY -= bulletYChange
    
    player(playerX,playerY)
    gameScore(textX,textY)
    pygame.display.update()
        