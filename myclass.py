class Dot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


class Ship:
    def __init__(self, dot, length=1, orientation='h'):
        self.dot = dot
        self.length = length
        self.orientation = orientation
        self.lives = length

    def dots(self):
        _dots = [self.dot]
        if self.length > 1:
            for i in range(1, self.length):
                if self.orientation == 'h':
                    _dots.append(Dot(self.dot.y, self.dot.x + i))
                if self.orientation == 'v':
                    _dots.append(Dot(self.dot.y + i, self.dot.x))
        return _dots


class Board:
    def __init__(self, name_owner, field, ships, living_ships, hid=True):
        self.name_owner = name_owner
        self.field = field
        self.ships = ships
        self.living_ships = living_ships
        self.hid = hid

    def add_ship(self, dots):
        for dot in dots:
            if self.field[dot.y - 1][dot.x - 1] != '0':  # checking the ship's location points
                return False
        for dot in dots:
            self.field[dot.y - 1][dot.x - 1] = '■'

    def contour(self):
        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                if self.field[y][x] == '■':
                    if x + 1 < 6:
                        if self.field[y][x + 1] != '■':
                            self.field[y][x + 1] = '-'  # right
                    if y + 1 < 6:
                        if self.field[y + 1][x] != '■':
                            self.field[y + 1][x] = '-'  # down
                    if x - 1 >= 0:
                        if self.field[y][x - 1] != '■':
                            self.field[y][x - 1] = '-'  # left
                    if y - 1 >= 0:
                        if self.field[y - 1][x] != '■':
                            self.field[y - 1][x] = '-'  # up

    def print_board(self):
        if self.name_owner == 'player':
            print('поле игрока:')
        if self.name_owner == 'computer':
            print('поле компьютера:')
        print('  |', end=' ')
        for i in range(1, len(self.field[0]) + 1):
            print(i, '|', end=' ')
        print('\n', end='')
        for ny, y in enumerate(range(len(self.field))):
            print(ny + 1, '|', end=' ')
            for x in range(len(self.field[y])):
                print(self.field[y][x], '|', end=' ')
            print('\n', end='')
        return ''

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
        self.ai_bord = ai_bord

    def random_board(self):
        pass

    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass
