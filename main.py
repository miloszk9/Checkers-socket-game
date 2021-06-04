import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT, ROWS, COLS
from board import Board
from network import Network


def clicked_pos(position):
    return int(position[0]/(WIDTH/ROWS)), int(position[1]/(HEIGHT/COLS))

def flip_coords(x, y):
    # Function to flip coords before sending data to opponent
    # e.g (0,0) -> (7,7), (2,4) -> (5,3) 
    return abs(7 - x), abs(7 - y)

def flip_coords_list(list):
    flipped = []
    for item in range(len(list)):
        flipped.append(flip_coords(list[item][0], list[item][1]))

    return flipped

def kill_piece(x, y):
    board.board_pieces[y][x] = None

def turn(x, y, piece_clicked):
    global my_turn

    print("kill list: ", board.available_kills())


    if not piece_clicked: # When user is going to click a pawn
        if board.is_player_piece(x, y):
            print('Piece clicked')
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
            elif board.is_player_piece(x, y):
                print('Piece clicked')
                moves = board.check_moves(x, y) # moves - tuple containing available moves - x,y coords
                print(moves)
                return {'coords': (x, y), 'moves': moves}
            else:
                print('User clicked opponent pawn')
                board.color_board()
                return None
        elif board.is_player_piece(x, y) == False:
            available_kills_list = board.available_kills()
            pieces_we_can_kill = []
            to_kill = []

            if len(available_kills_list) == 0: # player doesnt have possibility of killing
                if (x, y) in piece_clicked['moves']:
                    print('Moved')
                    board.color_board()
                    board.move_piece(*piece_clicked['coords'], x, y)
                    network.send((*flip_coords(*piece_clicked['coords']), *flip_coords(x, y)))
                    my_turn = False
                    return None
                else:
                    return piece_clicked
            else: #player has to kill piece
                for item in range(len(available_kills_list)):
                    if (available_kills_list[item][0], available_kills_list[item][1]) == (piece_clicked['coords'][0], piece_clicked['coords'][1]):
                        pieces_we_can_kill.append((available_kills_list[item][2][0][0], available_kills_list[item][2][0][1]))
                
                if (x, y) in pieces_we_can_kill:
                    x_killed = (piece_clicked['coords'][0] + x)/2
                    y_killed = (piece_clicked['coords'][1] + y)/2

                    print("x_killed", x_killed, "y_killed", y_killed)

                    kill_piece(int(x_killed),int(y_killed))
                    to_kill.append([int(x_killed),int(y_killed)])
                    board.color_board()
                    board.move_piece(*piece_clicked['coords'], x, y)
                    network.send((*flip_coords(*piece_clicked['coords']), *flip_coords(x, y), flip_coords_list(to_kill))) #added killed pieces coords (list) in send data
                    my_turn = False
                    return None
                else:
                    print("YOU HAVE TO SLAUGHTER THE ENEMY FIRST BRO")
                    return piece_clicked

        else:
            print('Not Moved')
            return piece_clicked

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

        board.draw_board(WINDOW)
        board.draw_pieces(WINDOW)
        if(piece_clicked):
            pygame.draw.circle(WINDOW, (255,255,255), (piece_clicked['coords'][0]*SQUARE_SIZE+SQUARE_SIZE/2, 
                                                       piece_clicked['coords'][1]*SQUARE_SIZE+SQUARE_SIZE/2), 10)
        pygame.display.update()

        if my_turn == False:
            #print('Wait for response...')
            data_recive = network.recive()
            
            if data_recive is not None and len(data_recive) > 0:
                print("Recieved data: ", data_recive)
                board.move_piece(data_recive[0], data_recive[1], data_recive[2], data_recive[3])
                #print(data_recive)
                if len(data_recive) > 4:
                    kill_piece(data_recive[4][0][0], data_recive[4][0][1])
                my_turn = True

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
