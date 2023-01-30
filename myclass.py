class Dot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


class Ship:
    def __init__(self, y, x, length=1, orientation='h'):
        self.y = y
        self.x = x
        self.length = length
        self.orientation = orientation
        self.lives = length

    def dots(self):
        _dots = [[self.y, self.x]]
        if self.length > 1:
            for i in range(1, self.length):
                if self.orientation == 'h':
                    _dots.append([self.y, self.x + i])
                if self.orientation == 'v':
                    _dots.append([self.y + i, self.x])
        return _dots
