class Dot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f'[y:{self.y} x:{self.x}]'

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

    def add_ship(self, dots):  # доработать, добавить исключения размещение вне поля
        for dot in dots:
            if self.field[dot.y][dot.x] != '0':  # checking the ship's location points
                return False
        for dot in dots:
            self.field[dot.y][dot.x] = '■'

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

    def print_board(self):  # доработать, вывод в зависимости от параметра hid
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

    @staticmethod
    def out(dot):
        if dot.y < 0 or dot.y > 5 or dot.x < 0 or dot.x > 5:
            return False
        return True

    def shot(self, dot):
        if not Board.out(dot):
            return False
        if self.field[dot.y][dot.x] == 'X' or self.field[dot.y][dot.x] == 'T':
            return False
        if self.field[dot.y][dot.x] == '■':
            self.field[dot.y][dot.x] = 'X'
        else:
            self.field[dot.y][dot.x] = 'T'
        return True


class Player:
    def __init__(self, self_board=Board, opponent_board=Board):
        self.self_board = self_board
        self.opponent_board = opponent_board

    def ask(self):
        while True:
            try:
                hit_yx_ = list(map(int, input('Удар игрока y, x: ').split()))
            except ValueError:
                print('Введите через пробел y, x в диапазоне от 1 до 6:')
                continue
            if len(hit_yx_) != 2:
                print('Введите две цифры через пробел:')
                continue
            dot = Dot(hit_yx_[0] - 1, hit_yx_[1] - 1)
            if not Board.out(dot):
                print('Введите y, x в диапазоне от 1 до 6:')
                continue
            if self.opponent_board.field[dot.y][dot.x] == 'X':
                print('Повтор, введите другие координаты y, x:')
                continue
            #    field_computer_[y_ - 1][x_ - 1] == 'T'):
            break
        if self.opponent_board.field[dot.y][dot.x] == '■':
            self.opponent_board.field[dot.y][dot.x] = 'X'
        else:
            self.opponent_board.field[dot.y][dot.x] = 'T'
        return True


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
