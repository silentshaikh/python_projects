import turtle
import time
#create a window for game
gameWindow = turtle.Screen()
gameWindow.title("Png Game By SAM")
gameWindow.bgcolor("skyblue")
gameWindow.setup(width=800,height=600)
gameWindow.tracer(0)

# Sore 
scoreA = 0
scoreB = 0


# paddle A

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)




# paddle B


paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)



# Ball

gameBall = turtle.Turtle()
gameBall.speed(0)
gameBall.shape("circle")
gameBall.color("teal")
gameBall.penup()
gameBall.goto(0,0)
gameBall.dx = 2
gameBall.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0 Player B : 0",align="center",font=("Courier",24,"normal"))

def paddleAUp():
    y = paddleA.ycor()
    y +=20
    paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    y -=20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y +=20
    paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    y -=20
    paddleB.sety(y)

gameWindow.listen()
gameWindow.onkeypress(paddleAUp,"w")
gameWindow.onkeypress(paddleADown,"s")
gameWindow.onkeypress(paddleBUp,"Up")
gameWindow.onkeypress(paddleBDown,"Down")



while True:
    gameWindow.update()
    time.sleep(0.01)
    # move the ball
    gameBall.setx(gameBall.xcor()+gameBall.dx)
    gameBall.sety(gameBall.ycor()+gameBall.dy)

    #border checking
    if gameBall.ycor() > 290:
        gameBall.sety(290)
        gameBall.dy *= -1
    
    if gameBall.ycor() < -290:
        gameBall.sety(-290)
        gameBall.dy *= -1
    
    if gameBall.xcor() > 390:
        gameBall.goto(0,0)
        gameBall.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A : {scoreA} Player B : {scoreB}",align="center",font=("Courier",24,"normal"))
    
    if gameBall.xcor() < -390:
        gameBall.goto(0,0)
        gameBall.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A : {scoreA} Player B : {scoreB}",align="center",font=("Courier",24,"normal"))

    
    # paddle and ball collissions
    if (gameBall.xcor() > 340 and gameBall.xcor() < 350) and (gameBall.ycor() < paddleB.ycor()+50 and gameBall.ycor() > paddleB.ycor()-40):
        gameBall.setx(340)
        gameBall.dx *= -1
    

    if (gameBall.xcor() < -340 and gameBall.xcor() > -350) and (gameBall.ycor() < paddleA.ycor()+50 and gameBall.ycor() > paddleA.ycor()-40):
        gameBall.setx(-340)
        gameBall.dx *= -1
    



