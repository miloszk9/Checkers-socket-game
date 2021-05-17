import numpy as np


#Board definition 1-black, 0-white
board = np.zeros((8,8),dtype=int)
board[1::2,::2] = 1
board[::2,1::2] = 1



def createPieces():
    piecesList = []
    for i in range(24):
        if i < 12:
            pos = startingPosition(i)
            piece = {
                "id": i,
                "color": "white",
                "posX": pos[0],
                "posY": pos[1],
                "isAlive": False,
                "isSuper": False 
            }
            piecesList.append(piece)
            print(piece)
        else:
            pos = startingPosition(i)
            piece = {
                "id": i,
                "color": "black",
                "posX": pos[0],
                "posY": pos[1],
                "isAlive": False,
                "isSuper": False 
            }
            piecesList.append(piece)
            print(piece)

 
def startingPosition(id):
    startingList = []
    index = 0
    for row in board:
        indey = 0
        for cell in row:
            if 0 <= index <= 2 or 5 <= index <= 7:
                if cell == 1:
                    startingList.append([index, indey])
            indey += 1
        index += 1

    return startingList[id]

createPieces()



