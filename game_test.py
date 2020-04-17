import pygame, drawings, board, square, rules, actions

pygame.init()
pygame.display.set_caption("Super checkers")

NUM_OF_BOARDS = 1
BOARD_SIZE = 600


def build_boards(howmany, size):
    names = ['game'] + ['meta ' * i + 'rules' for i in range(howmany)]
    brds = [board.Board(size, (size * i + 20 * (2 * i + 1), 20), names[i]) for i in range(howmany)]
    return brds


no_sqr_chosen = square.Square((-1, -1), (0, 0, 0)), []


# initial conditions
win = pygame.display.set_mode(((BOARD_SIZE + 40) * NUM_OF_BOARDS, BOARD_SIZE + 40))
boards = build_boards(NUM_OF_BOARDS, BOARD_SIZE)
chosen_sqr, legal_squares_to_move = no_sqr_chosen
turn = 1  # white's turn
# GUI
drawings.update_gui(win, boards, chosen_sqr,legal_squares_to_move)

# the game itself
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(chosen_sqr.pos)

            # If a legal squares to move has been clicked, move the according piece and change the turn.
            # The legal_squares_to_move and chosen_sqr were set in the previous loop.
            for sqr in legal_squares_to_move:
                if sqr.in_square(pos):
                    actions.move_piece(chosen_sqr, sqr, b)
                    chosen_sqr, legal_squares_to_move = no_sqr_chosen
                    turn *= (-1)
                    continue

            # Call the chosen square "chosen_sqr".
            for b in boards:
                if b.clicked_sqr(pos).piece is not None:
                    if b.clicked_sqr(pos).piece.color == turn:
                        chosen_sqr = b.clicked_sqr(pos)

            # list all the legal places for the piece in the chosen square
            legal_squares_to_move = rules.legal_moves_2(chosen_sqr, b)

            drawings.update_gui(win, boards, chosen_sqr, legal_squares_to_move)
    pygame.display.update()

pygame.quit()  # If we exit the loop this will execute and close our game

print('Goodbye!')
