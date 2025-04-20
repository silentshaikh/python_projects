import pygame
from network import Network
width = 500
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

# clientNumber =0




# def readPos(str:str):
#     str = str.split(",")
#     return int(str[0]), int(str[1])


# def makePos(tup):
#     return str(tup[0]) + "," + str(tup[1])
# pos = [(0,0),(100,100)]

class Button:
    def __init__(self,text,x,y,color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self,width,self.height))
        font = pygame.font.SysFont('comicsons',40)
        text = font.render(self.text,1,(255,255,255))
        win.blit(text,(self.x + round(self.width/2) - round(text.get_width()/2),self.y + round(self.height/2) - round(text.get_height()/2)))
    
    def click(self,pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False




def reDrawWindow(win,game,p):
    win.fill((128,128,128))
    # player.draw(win)
    # player2.draw(win)
    # pygame.display.update()
    if not game.connected():
        font = pygame.font.SysFont('comicsons',80)
        text= font.render("Waiting for PLayer ...",1,(255,0,0),True)
        win.blit(text,(width/2 -  text.get_width()/2,height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont('comicsons',60)
        text= font.render("Your Move",1,(0,255,255))
        win.blit(text,(80,100))

        text= font.render("Opponents",1,(0,255,255))
        win.blit(text,(380,200))

        move1 = game.getPlayerMove(0)
        move2 = game.getPlayerMove(1) 
        if game.bothWent():
            text1 = font.render(move1,1,(0,0,0))
            text3 = font.render(move2,1,(0,0,0))
        else:
            if game.p1Went and p==0:
                text1 = font.render(move1,0,(0,0,0))
            elif game.p1Went:
                text1 = font.render("Locked In ",0,(0,0,0))
            else:
                text1 = font.render("Waiting...",0,(0,0,0))

            if game.p2Went and p==1:
                text2 = font.render(move2,0,(0,0,0))
            elif game.p2Went:
                text2 = font.render("Locked In ",0,(0,0,0))
            else:
                text2 = font.render("Waiting...",0,(0,0,0))
            
        if p == 1:
            win.blit(text2,(100,350))
            win.blit(text1,(400,350))
        else:
            win.blit(text1,(100,350))
            win.blit(text2,(400,350))

        for btn in btnList:
            btn.draw(win)
    
    pygame.display.update()



        






btnList = [Button("Rock",50,500,(0,0,0)),Button("Scissors",250,500,(255,0,0)),Button("Paper",450,500,(0,255,0))]

def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    player = int(n.getP())
    print(f"You are PLayer {player}")

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            reDrawWindow(win,game,player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break
            font = pygame.font.SysFont('comicsons',90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text= font.render("You Won !",1, (255,0,0))
            elif game.winner() == -1:
                text= font.render("Tie Game !",1, (255,0,0))
            else:
                text= font.render("You Lost ...",1, (255,0,0))
            win.blit(text,(width/2 - text.get_width()/2 , height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btnList:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)

                        else:
                            if not game.p2Went:
                                n.send(btn.text)
        reDrawWindow(win,game,player)



    # run = True
    # # startPos = readPos(n.getPos())
    # # p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    # # p2 = Player(0,0,100,100,(255,0,0))

    # while run:
    #     clock.tick(60)
    #     p2 = n.send(p)
    #     # p2Pos = readPos(n.send(makePos((p.x,p.y))))
    #     # p2.x = p2Pos[0]
    #     # p2.y = p2Pos[1]
    #     # p2.update()
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #             pygame.quit()
    #     p.move()
    #     reDrawWindow(win,p,p2)


def menuScreen():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        font = pygame.font.SysFont('comicsons',60)
        win.fill((128,128,128))
        text= font.render("Click to Play :",1, (255,0,0))
        win.blit(text,(100,200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run =  False
            
            if event.type == pygame.MOUSEBUTTONDOWN :
                run = False
    main()



# main()

while True:
    menuScreen()