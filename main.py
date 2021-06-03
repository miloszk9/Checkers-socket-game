import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT, ROWS, COLS
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
    if not piece_clicked: # We want to click an empty space
        if board.is_piece(x, y): # We want to click a piece
            print('Piece clicked')
            # TODO: change piece_clicked to dict - with 'clicked_coords', and 'available_moves'
            # Dont flip entire board, just send reverse coords to opponent
            moves = board.check_moves(x, y) # moves - tuple containing available moves - x,y coords
            print(moves)
            return {'coords': (x, y), 'moves': moves}
        else:
            print('Piece not clicked')
            return None
    else:
        if board.is_piece(x, y):
            if piece_clicked['coords'][0] == x and piece_clicked['coords'][1] == y:
                print('Piece unclicked')
                board.color_board()
                return None        
            else:
                print('Piece clicked')
                moves = board.check_moves(x, y) # moves - tuple containing available moves - x,y coords
                print(moves)
                return {'coords': (x, y), 'moves': moves}
        elif board.is_piece(x, y) == False:
            if (x, y) in piece_clicked['moves']:
                print('Moved')
                board.color_board()
                board.move_piece(*piece_clicked['coords'], x, y)
                return None
            else:
                return piece_clicked
        else:
            print('Not Moved')
            return piece_clicked

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
        if(piece_clicked):
            pygame.draw.circle(WINDOW, (255,255,255), (piece_clicked['coords'][0]*SQUARE_SIZE+SQUARE_SIZE/2, 
                                                       piece_clicked['coords'][1]*SQUARE_SIZE+SQUARE_SIZE/2), 10)
        pygame.display.update()

    pygame.quit()
