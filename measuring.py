def distance(sqr1, sqr2):
    return max(abs(sqr1.pos[0] - sqr2.pos[0]), abs(sqr1.pos[1] - sqr2.pos[1]))


def direction(sqr1, sqr2):
    if sqr1.pos[0] == sqr2.pos[0] or sqr1.pos[1] == sqr2.pos[1]:
        return 'straight'
    if ((sqr1.pos[0] - sqr2.pos[0]) / (sqr1.pos[1] - sqr2.pos[1])) ** 2 == 1:
        return 'diagonal'


def not_lower_than(sqr1, sqr2):
    if sqr1.pos[0] <= sqr2.pos[0]:
        return 1
    return -1


def between(sqr1, sqr2, sqr3):  # whether sqr3 is between sqr1 and sqr2
    if direction(sqr1, sqr2) == direction(sqr1, sqr3) and direction(sqr1, sqr2) is not None:
        if ((sqr3.pos[0] - sqr1.pos[0]) * (sqr3.pos[0] - sqr2.pos[0])) < 0 \
                and ((sqr3.pos[1] - sqr1.pos[1]) * (sqr3.pos[1] - sqr2.pos[1])) < 0:
            return True
    return False


def enemies(sqr1, sqr2):
    if sqr1.piece is not None and sqr2.piece is not None:
        return sqr1.piece.color * sqr2.piece.color == -1


def enemies_between(sqr1, sqr2, brd):
    return [sqr for sqr in brd.all_squares() if between(sqr1, sqr2, sqr) and enemies(sqr1, sqr)]


def pieces_in_row(row, brd):
    pieces = [sqr.piece for sqr in brd.squares[row] if sqr.piece is not None]
    return len(pieces)


# move-testing functions
def normal_move(sqr1, sqr2, regular_rules):
    if sqr1.piece is not None and sqr2.piece is None:
        if not_lower_than(sqr1, sqr2) * sqr1.piece.color == -1:  # if the higher piece is black
            if distance(sqr1, sqr2) == regular_rules['step_size'] \
                    and direction(sqr1, sqr2) == regular_rules['direction']:
                return True
    return False


def eating_move(sqr1, sqr2, brd, regular_rules):
    if sqr1.piece is not None and sqr2.piece is None:
        if not_lower_than(sqr1, sqr2) * sqr1.piece.color == -1:  # if the higher piece is black
            if distance(sqr1, sqr2) <= regular_rules['step_size'] + 1 \
                    and direction(sqr1, sqr2) == regular_rules['direction']:
                if enemies_between(sqr1, sqr2, brd):
                    return True
    return False


def legal_moves(sqr1, brd, regular_rules):
    normal_moves = [sqr for sqr in brd.all_squares() if normal_move(sqr1, sqr, regular_rules)]
    eating_moves = [sqr for sqr in brd.all_squares() if eating_move(sqr1, sqr, brd, regular_rules)]
    return normal_moves + eating_moves


'''
rules = {'dist': lambda sqr1, sqr2: step_size == distance(sqr1, sqr2),
         'direc': lambda sqr1, sqr2: direc == direction(sqr1, sqr2),
         'forward': lambda sqr1, sqr2: not_lower_than(sqr1, sqr2) != sqr1.piece.color
                                                if sqr1.piece is not None else None,
         'empty': lambda sqr1, sqr2: True if sqr2.piece is None else False}


def legal_move(sqr1, sqr2):
    if sqr1.piece is None:
        return False
    is_legal = True
    for rule in regular_rules:
        if not regular_rules[rule](sqr1, sqr2):
            is_legal = False
            break
    return is_legal
'''
