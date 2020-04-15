class Square:
    def __init__(self, position, color, piece=None, coords=(0,0), size=None):
        self.pos = position
        self.coords = int(coords[0]), int(coords[1])
        self.size = size
        self.color = color
        self.piece = piece

    def __str__(self):
        return 'pos: {}, color: {}, piece: ({})'.format(self.pos, self.color, self.piece)

    def in_square(self, some_coords):
        return (self.coords[0] < some_coords[0] < self.coords[0] + self.size) \
               and (self.coords[1] < some_coords[1] < self.coords[1] + self.size)



