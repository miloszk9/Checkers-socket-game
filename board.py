import numpy as np
from pygame import draw
from piece import Piece
import pygame
from constants import BLACK, BRIGHT, BRIGHT, COLS, DARK, ROWS, SQUARE_SIZE, WHITE

class Board:
    def __init__(self):
        self.board_color = []
        self.board_pieces = []
        self.starting_list = []
        self.color_board()
        self.create_board()


    #Board definition 1-black, 0-white
    def color_board(self):
        self.board_color = np.zeros((8,8),dtype=int)
        self.board_color[1::2,::2] = 1
        self.board_color[::2,1::2] = 1

    def create_board(self):
        self.board_pieces = ([], [], [], [], [], [], [], [])
        for i in range(8):
            for _ in range(8):
                self.board_pieces[i].append(None)
        for i in range(24):
            if i < 12:
                pos = self.starting_position(i)
                piece = Piece(i, pos[0], pos[1], "white", WHITE)
                self.board_pieces[pos[0]][pos[1]] = piece
                print("ID: ", i, "column: ", piece.col, "row: ", piece.row ,"color: ", piece.color, " created")
            else:
                pos = self.starting_position(i)
                piece = Piece(i, pos[0], pos[1], "black", BLACK)
                self.board_pieces[pos[0]][pos[1]] = piece
                print("ID: ", i, "column: ", piece.col, "row: ", piece.row ,"color: ", piece.color, " created")

    def starting_position(self, id): 
        index = 0
        for row in self.board_color:
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
        for row in range(8):
            for col in range(8):
                if self.board_pieces[row][col] is not None:
                    window.blit(self.board_pieces[row][col].image,
                                pygame.Rect(self.board_pieces[row][col].col*SQUARE_SIZE,
                                self.board_pieces[row][col].row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def is_piece(self, x, y):
        pass

# s = Board()
