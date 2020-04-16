import pygame, math


def draw_boards(win, brds):
    for brd in brds:
        for row in brd.squares:
            for sqr in row:
                draw_square(win, sqr)


def draw_square(win, sqr):
    x, y = sqr.coords[0], sqr.coords[1]
    color = 255 * (sqr.color + 1) / 2
    pygame.draw.rect(win, (color, color, color), (x, y, sqr.size, sqr.size))


def draw_piece(win, sqr):
    size = sqr.size // 3
    color = 255 * (sqr.piece.color + 1) / 2
    x, y = sqr.coords[0] + sqr.size//2, sqr.coords[1] + sqr.size//2
    pygame.draw.circle(win, (0, 0, 0), (x, y), size, int(size*0.2))
    pygame.draw.circle(win, (color, color, color), (x, y), math.ceil(size*0.8), math.ceil(size*0.8))


def draw_all_pieces(win, brds):
    for brd in brds:
        for row in brd.squares:
            for sqr in row:
                if sqr.piece is not None:
                    draw_piece(win, sqr)


def update_gui(win, boards, chosen_sqr, options):
    win.fill((80, 80, 80))
    draw_boards(win, boards)
    for sqr in options:
        mark_square(win, sqr)
    draw_all_pieces(win, boards)
    mark_piece(win, chosen_sqr)


def mark_piece(win, sqr):
    if sqr.piece is not None:
        x, y = sqr.coords[0] + sqr.size // 2, sqr.coords[1] + sqr.size // 2
        size = sqr.size // 3
        pygame.draw.circle(win, (255, 0, 0), (x, y), size, int(size * 0.2))
        pygame.display.update()


def mark_square(win, sqr):
    x, y = sqr.coords
    pygame.draw.polygon(win, (255, 0, 0),
                       ((x, y), (x + sqr.size, y), (x + sqr.size, y + sqr.size), (x, y + sqr.size)), 4)
    pygame.display.update()
