import drawings


def move_piece(sqr1, sqr2):
    sqr2.piece = sqr1.piece
    sqr1.piece = None
    # drawings.draw_square(sqr1)
