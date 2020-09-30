import pygame

from board import Board


def main():
    screen = pygame.display.set_mode((1000, 500))
    board = Board("hej", "hej", 0, [200, 200, 200], screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                print(board.deck.get_pos(mouse_x, mouse_y))

        screen.fill([0, 0, 0])
        board.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
