import rules


def move_piece(orig, dest, brd):  # also eats any enemies in between
    for sqr in rules.enemies_between(orig, dest, brd):
        sqr.piece = None
    dest.piece = orig.piece
    orig.piece = None