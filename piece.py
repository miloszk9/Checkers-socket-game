class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.super = False
        self.dead = False

    
    def make_king(self):
        self.super = True
    
    def make_dead(self):
        self.dead = False

    def move(self, row, col):
        self.row = row
        self.col = col
