import pygame
from constants import WIDTH, HEIGHT, ROWS, COLS
from board import Board
from network import Network


def clicked_pos(position):
    return int(position[0]/(WIDTH/ROWS)), int(position[1]/(HEIGHT/COLS))

def turn(x, y, piece_clicked):
    global my_turn

    if piece_clicked: # We want to click an empty space
        if board.is_piece(x, y) == False:
            print('Moved')
            board.move_piece(*piece_clicked, x, y)
            network.send((*piece_clicked, x, y))
            my_turn = False
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

def main():
    global board, my_turn

    my_turn = network.connect()
    
    if my_turn:
        _ = network.recive()

    send = False
    run = True
    piece_clicked = None

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if my_turn == True:
                    pos = pygame.mouse.get_pos()
                    x, y =  clicked_pos(pos)
                    print("X: "+ str(x) + ' Y: ' + str(y))
                    piece_clicked = turn(x, y, piece_clicked)
                    print('Piece clicked: '+str(piece_clicked))

        board.draw_board(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()

        if my_turn == False:
            print('Wait for response...')
            data_recive = network.recive()
            board.move_piece(*data_recive)
            my_turn = True

    network.disconnect()
    pygame.quit()
    quit()

if __name__ == '__main__':
    '''
    consts for window
    '''
    FPS = 15
    programIcon = pygame.image.load('assets/icon.png')

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Warcaby')
    pygame.display.set_icon(programIcon)

    '''
    Game global variables
    '''
    clock = pygame.time.Clock()
    board = Board()
    my_turn = None

    network = Network()

    main()
