import rules, drawings


def move_piece(sqr1, sqr2): # also eats any enemies in between
    sqr2.piece = sqr1.piece
    sqr1.piece = None
    for sqr in rules.enemies_between(sqr1, sqr2):
        sqr.piece = None
