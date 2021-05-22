import numpy as np
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.starting_list = []
        self.create_board()
        self.create_pieces()


    #Board definition 1-black, 0-white
    def create_board(self):
        self.board = np.zeros((8,8),dtype=int)
        self.board[1::2,::2] = 1
        self.board[::2,1::2] = 1

    def create_pieces(self):
        pieces_list = []
        for i in range(24):
            if i < 12:
                pos = self.starting_position(i)
                piece = Piece(pos[0], pos[1], "white")
                pieces_list.append(piece)
                print("ID: ", i, "column: ", piece.col, "row: ", piece.row ,"color: ", piece.color, " created")
            else:
                pos = self.starting_position(i)
                piece = Piece(pos[0], pos[1], "black")
                pieces_list.append(piece)
                print("ID: ", i, "column: ", piece.col, "row: ", piece.row ,"color: ", piece.color, " created")

    def starting_position(self, id): 
        index = 0
        for row in self.board:
            indey = 0
            for cell in row:
                if 0 <= index <= 2 or 5 <= index <= 7:
                    if cell == 1:
                        self.starting_list.append([index, indey])
                indey += 1
            index += 1

        return self.starting_list[id]

s = Board()
