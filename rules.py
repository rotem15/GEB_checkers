initial_rules = {'step_size': 1,
                 'direction': 'diagonal',
                 'go_back': False,
                 'add_piece': False,
                 'rotate_board': False,  # queen_is_born
                 'num_of_moves': 1}


def pieces_in_row(row, brd):
    return len([sqr for sqr in brd.squares[row] if sqr.piece is not None])


def decide_direc(rules_board):
    options = ['diagonal', 'straight']
    return options[pieces_in_row(0, rules_board) % 2]


def update_rules(rules_board):
    rules_dic = {'step_size': 5 - pieces_in_row(7, rules_board),
                 'direction': decide_direc(rules_board),
                 'go_back': False,
                 'add_piece': False,
                 'rotate_board': False,  # queen_is_born
                 'num_of_moves': 1}  # sqrt(middle_rows + 1)
    return rules_dic


# measuring functions
