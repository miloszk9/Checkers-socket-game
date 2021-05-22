import numpy as np
from pygame import draw
from piece import Piece
import pygame
from constants import BLACK, BRIGHT, BRIGHT, COLS, DARK, ROWS, SQUARE_SIZE, WHITE

class Board:
    def __init__(self):
        self.board = []
        self.starting_list = []
        self.pieces_list = []
        self.create_board()
        self.create_pieces()


    #Board definition 1-black, 0-white
    def create_board(self):
        self.board = np.zeros((8,8),dtype=int)
        self.board[1::2,::2] = 1
        self.board[::2,1::2] = 1

    def create_pieces(self):
        for i in range(24):
            if i < 12:
                pos = self.starting_position(i)
                piece = Piece(pos[0], pos[1], "white", WHITE)
                self.pieces_list.append(piece)
                print("ID: ", i, "column: ", piece.col, "row: ", piece.row ,"color: ", piece.color, " created")
            else:
                pos = self.starting_position(i)
                piece = Piece(pos[0], pos[1], "black", BLACK)
                self.pieces_list.append(piece)
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

    def draw_board(self, window):
        window.fill(DARK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, BRIGHT, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, window):
        for piece in self.pieces_list:
            window.blit(piece.image, pygame.Rect(piece.col*SQUARE_SIZE, piece.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


# s = Board()
