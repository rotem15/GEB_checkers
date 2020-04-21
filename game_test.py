import pygame, drawings, board, square, rules, actions, measuring

NUM_OF_BOARDS = 2
BOARD_SIZE = 800


def build_boards(howmany, size):
    names = ['game', 'rules', 'meta rules']
    shown_brds = [board.Board(size, (size * i + 20 * (2 * i + 1), 20), names[i]) for i in range(howmany)]
    hidden_brds = [board.Board(size, (size * i + 20 * (2 * i + 1), 20), names[i]) for i in range(howmany, 3)]
    return shown_brds, hidden_brds


# initial conditions
no_sqr_chosen = square.Square((-1, -1), (0, 0, 0)), board.Board(), []
win = pygame.display.set_mode(((BOARD_SIZE + 40) * NUM_OF_BOARDS, BOARD_SIZE + 40))
shown_boards, hidden_boards = build_boards(NUM_OF_BOARDS, BOARD_SIZE)
game_board, rules_board, meta_rules_board = shown_boards + hidden_boards
chosen_sqr, chosen_board, legal_squares_to_move = no_sqr_chosen
turn = 1  # white's turn

# the game itself
pygame.init()
pygame.display.set_caption("Super checkers")
drawings.update_gui(win, shown_boards, chosen_sqr, legal_squares_to_move)

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            regular_rules = rules.update_rules(rules_board)
            meta_rules = rules.update_rules(meta_rules_board)

            # If a legal squares to move has been clicked, move the according piece and change the turn.
            # The legal_squares_to_move and chosen_sqr were set in the previous loop.
            for sqr in legal_squares_to_move:
                if sqr.in_square(pos):
                    actions.move_piece(chosen_sqr, sqr, chosen_board)
                    chosen_sqr, chosen_board, legal_squares_to_move = no_sqr_chosen
                    turn *= (-1)
                    continue

            # Call the chosen square "chosen_sqr".
            for b in shown_boards:
                if b.clicked_sqr(pos).piece is not None:
                    if b.clicked_sqr(pos).piece.color == turn:
                        chosen_board = b
                        chosen_sqr = b.clicked_sqr(pos)

            # list all the legal places for the piece in the chosen square
            if chosen_sqr in game_board.all_squares():
                legal_squares_to_move = measuring.legal_moves(chosen_sqr, chosen_board, regular_rules)
            if chosen_sqr in rules_board.all_squares():
                legal_squares_to_move = measuring.legal_moves(chosen_sqr, chosen_board, rules.initial_rules)

            drawings.update_gui(win, shown_boards, chosen_sqr, legal_squares_to_move)
    pygame.display.update()

pygame.quit()  # If we exit the loop this will execute and close our game

print('Goodbye!')
