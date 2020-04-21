import piece, square


class Board:
    def __init__(self, size=100, top_left=(0, 0), name='game'):
        self.name = name
        self.size = size
        self.top_left = top_left
        self.squares = [[square.Square((i, j), -1 + 2*((j+i) % 2)) for j in range(8)] for i in range(8)]
        self.set_squares()
        self.set_pieces()

    def set_squares(self):
        y = self.top_left[1]
        for row in self.squares:
            x = self.top_left[0]
            for sqr in row:
                sqr.coords = (x, y)
                sqr.size = self.size // 8
                x += sqr.size
            y += sqr.size

    def set_pieces(self):
        id = 0
        for row in enumerate(self.squares):
            if row[0] not in (3, 4):
                for sqr in row[1]:
                    if sqr.color == 1:
                        color = -1 + 2*(row[0] // 4)
                        sqr.piece = piece.Piece(color, color * (id % 12+1))
                        id += 1

    def all_squares(self):
        all_s = []
        for row in self.squares:
            for sqr in row:
                all_s.append(sqr)
        return all_s

    def clicked_sqr(self, pos):
        for sqr in self.all_squares():
            if sqr.in_square(pos):
                return sqr
        return square.Square((-1, -1), (0, 0, 0))

