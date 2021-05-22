import pygame
from constants import WIDTH, HEIGHT
from board import Board

'''
consts for window
'''
FPS = 1
programIcon = pygame.image.load('assets/icon.png')


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')
pygame.display.set_icon(programIcon)


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        board.draw_board(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()

    pygame.quit()

main()
