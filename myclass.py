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


class Board:
    def __init__(self, field, ships, living_ships, hid):
        self.field = field
        self.ships = ships
        self.living_ships = living_ships
        self.hid = hid

    def add_ship(self):
        pass

    def contour(self):
        pass

    def print_board(self):
        pass

    def out(self):
        pass


class Player:
    def __init__(self, self_board, opponent_board):
        self.self_board = self_board
        self.opponent_board = opponent_board

    def ask(self):
        pass

    def move(self):
        pass


class AI(Player):
    def ask(self):
        pass


class User(Player):
    def ask(self):
        pass


class Game:
    def __init__(self, user, user_bord, ai, ai_bord):
        self.user = user
        self.user_bord = user_bord
        self.ai = ai
        self.ai_bord =ai_bord

    def random_board(self):
        pass

    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass
