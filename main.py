import pygame
from constants import WIDTH, HEIGHT, ROWS, COLS
from board import Board

'''
consts for window
'''
FPS = 15
programIcon = pygame.image.load('assets/icon.png')


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')
pygame.display.set_icon(programIcon)


def clicked_pos(position):
    return int(position[0]/(WIDTH/ROWS)), int(position[1]/(HEIGHT/COLS))

def turn(x, y, piece_clicked):
    if piece_clicked: # We want to click an empty space
        if board.is_piece(x, y) == False:
            print('Moved')
            board.move_piece(*piece_clicked, x, y)
            return None
        else:
            print('Not Moved')
            return piece_clicked
    else:
        if board.is_piece(x, y): # We want to click a piece
            print('Piece clicked')
            return (x, y)
        else:
            print('Piece not clicked')
            return None

if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    board = Board()
    piece_clicked = None

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x, y =  clicked_pos(pos)
                print("X: "+ str(x) + ' Y: ' + str(y))
                piece_clicked = turn(x, y, piece_clicked)
                print('Piece clicked: '+str(piece_clicked))

        board.draw_board(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()

    pygame.quit()
