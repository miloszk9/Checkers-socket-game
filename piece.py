from constants import SQUARE_SIZE, WHITE


class Piece:

    def __init__(self, id, row, col, color, image):
        self.id = id
        self.row = row
        self.col = col
        self.color = color
        self.image = image
        self.super = False
        self.dead = False        
    
    def make_super(self):
        self.super = True
    
    def make_dead(self):
        self.dead = False

    def move(self, row, col):
        self.row = row
        self.col = col