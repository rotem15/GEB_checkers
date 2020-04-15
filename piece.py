class Piece:
    def __init__(self, color, id=0):
        self.color = color
        self.id = id
        self.is_queen = False

    def __str__(self):
        return 'color: {}, id: {}'.format(self.color, self.id)