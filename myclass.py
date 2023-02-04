import random
from accessify import protected


class Dot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __repr__(self):
        return f'[y{self.y},x{self.x}]'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


class Ship:
    def __init__(self, dot, length=1, orientation='h'):
        self.dot = dot
        self.length = length
        self.orientation = orientation
        self.lives = self.dots_protected()
        self.dots = self.dots_protected()

    picture = {3: '■■■', 2: '■■', 1: '■'}

    def __repr__(self):
        return f'ship:{self.picture[self.length]}'

    @protected
    def dots_protected(self):
        dots = [self.dot]
        if self.length > 1:
            for i in range(1, self.length):
                if self.orientation == 'h':
                    dots.append(Dot(self.dot.y, self.dot.x + i))
                if self.orientation == 'v':
                    dots.append(Dot(self.dot.y + i, self.dot.x))
        return dots


class Board:
    def __init__(self, name_owner, field, ships, living_ships, hid=True):
        self.name_owner = name_owner
        self.field = field
        self.ships = ships
        self.living_ships = living_ships
        self.hid = hid

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.field[dot.y][dot.x] != 'O':
                return False
        for dot in ship.dots:
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
            self.field[dot.y][dot.x] = 'x'  # проверка, первичная установка на доске
            for ship in self.ships:
                if dot in ship.dots:
                    self.ships[self.ships.index(ship)].lives.remove(dot)
                    self.field[dot.y][dot.x] = 'X'  # окончательная установка на доске
                    print('hit')
                    print(len(self.ships[self.ships.index(ship)].lives))
                    if len(self.ships[self.ships.index(ship)].lives) == 0:
                        self.living_ships.remove(ship)
                        print('kill')
                        print(self.living_ships)
            return True
        else:
            self.field[dot.y][dot.x] = 'T'
            return False


class Player:
    def __init__(self, self_board, opponent_board):
        self.self_board = self_board
        self.opponent_board = opponent_board

    def ask(self):
        pass

    def move(self):
        return self.opponent_board.shot(self.ask())


class AI(Player):
    def ask(self):  # доработать логику при следующем ударе после попадания
        while True:
            dot = Dot(random.randrange(6), random.randrange(6))
            # print('Удар ПК: ', dot)
            if (self.opponent_board.field[dot.y][dot.x] == 'X' or
                    self.opponent_board.field[dot.y][dot.x] == 'T'):
                continue
            else:
                break
        return dot


class User(Player):
    def ask(self):
        dot = Dot(9, 9)
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
                print('Введите через пробел y, x в диапазоне от 1 до 6:')
                continue
            if self.opponent_board.field[dot.y][dot.x] == 'X' or self.opponent_board.field[dot.y][dot.x] == 'T':
                print('Повтор, введите другие координаты y, x:')
                continue
            break
        return dot


class Game:
    def __init__(self, user, user_board, ai, ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board

    def random_board(self, board_, start_length_ships):
        board = board_
        for length in start_length_ships:
            while True:
                a = 0
                dot = Dot(random.randrange(6), random.randrange(6))
                ship = Ship(dot, length, random.choice('hv'))
                for dot in ship.dots:
                    if not board.out(dot) or board.field[dot.y][dot.x] != 'O':
                        a = 1
                if a == 1:
                    continue
                else:
                    break
            board.add_ship(ship)
            board.contour()
            board.ships.append(ship)
            board.living_ships.append(ship)
        if board.name_owner == 'player':
            self.user_board = board
        else:
            self.ai_board = board
        return True

    def greet(self, start_length_ships):

        dot = Dot(0, 0)
        ship = Ship(dot, 1)
        print(f'Вы имеете {len(start_length_ships)} кораблей, из них:')
        sum_length_ships = {'■■■': 0, '■■': 0, '■': 0}
        for length in start_length_ships:
            if length == 3:
                sum_length_ships['■■■'] += 1
            if length == 2:
                sum_length_ships['■■'] += 1
            if length == 1:
                sum_length_ships['■'] += 1
        print(sum_length_ships)
        print('Расставьте все ваши корабли на вашем игровом поле.\n'
              'Укажите координаты по "y" и по "x" через пробел.\n'
              'Координаты должны быть в диапазоне от 1 до 6.\n'
              'Укажите расположение Ваших кораблей по вертикали или горизонтали')
        for length in start_length_ships:
            while True:
                a = 0
                try:
                    ship_yx = list(map(int, input(f'Введите координаты первой точки "y" и "x" для '
                                                  f'{Ship.picture[length]}: ').split()))
                except ValueError:
                    print('Введите через пробел y, x в диапазоне от 1 до 6:')
                    continue
                if len(ship_yx) != 2:
                    print('Введите две цифры через пробел:')
                    continue
                orientation = input(f'введите "v" если корабль должен быть вертикальным'
                                    f' иначе он будет горизонтальным: ')
                if orientation != 'v':
                    orientation = 'h'
                dot = Dot(ship_yx[0] - 1, ship_yx[1] - 1)
                ship = Ship(dot, length, orientation)
                for dot in ship.dots:
                    if not Board.out(dot):
                        a = 1
                if a == 1:
                    print('Корабль вышел за границы игровой доски!!!\n'
                          'Введите через пробел y, x в диапазоне от 1 до 6:')
                    continue
                else:
                    if self.user_board.field[dot.y][dot.x] != 'O':
                        self.user_board.print_board()
                        print('Место занято!!!\n'
                              'Введите через пробел y, x в диапазоне от 1 до 6:')
                        continue
                    else:
                        break
            self.user_board.add_ship(ship)
            self.user_board.contour()
            self.user_board.print_board()
            self.user_board.ships.append(ship)
            self.user_board.living_ships.append(ship)

    def loop(self):  # сделать кто ходит первым через случай
        while True:
            while True:
                if self.user.move():
                    # print('check')
                    self.user_board.print_board()
                    self.ai_board.print_board()
                    continue
                else:
                    break
            while True:
                if self.ai.move():
                    # print('check')
                    continue
                else:
                    break
            self.user_board.print_board()
            self.ai_board.print_board()

    def start(self):
        pass
