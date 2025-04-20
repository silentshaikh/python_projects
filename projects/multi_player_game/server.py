import socket
from _thread import *
import sys
from game import Game
import pickle

server = "192.168.100.3"
port = 5555


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(f"Error binding server: {e}")
    sys.exit()

s.listen(2)
print("Waiting for a connection, Server Started")

# def readPos(str):
#     str  = str.split(",")
#     return int(str[0]), int(str[1])

# def makePos(tup):
#     return str(tup[0]) + "," + str(tup[1])
# pos = [(0,0),(100,100)]
# players = [Player(0,0,50,50,(255,0,0)),Player(100,100,50,50,(0,255,255))]

connected = set()
games = {}
idCount = 0


def threaded_client(conn,player):
    # conn.send(str.encode("Connected"))
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        data = conn.recv(4096).decode()
        try:

            if gameId in games:
                game = games[gameId]
                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p,data)
                    
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("Lost Connection")
    try:
        del games[gameId]
        print("Closing Game",gameId)
    except:
        pass

    idCount -=1
    conn.close()



            

# currentPlayer = 0

while True:
    conn,addr = s.accept()
    print("Connected to ",addr)

    idCount +=1
    p =0
    gameId = (idCount-1)//2
    if idCount % 2 ==1:
        games[gameId] = Game(gameId)
        print("Creating a new game")
    else:
        games[gameId].ready = True
        p =1

    start_new_thread(threaded_client,(conn,p))
    # currentPlayer += 1
