import random
from accessify import protected


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return 'Вы пытаетесь выстрелить за доску'


class BoardUserException(BoardException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку'


class BoardWrongShipException(BoardException):
    pass


class Dot:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __repr__(self):
        return f'Dot({self.y + 1},{self.x + 1})'

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x


class Ship:
    def __init__(self, dot, length=1, orientation='h'):
        self.dot = dot
        self.length = length
        self.orientation = orientation
        # self.lives = self.dots_protected()
        self.lives = len(self.dots_protected())
        self.dots = self.dots_protected()

    picture = {3: '■■■', 2: '■■', 1: '■'}

    def __repr__(self):
        return f'ship:{self.picture[self.length]} {self.dots}'

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

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, name_owner, hid=False, size=6):
        self.name_owner = name_owner
        self.hid = hid
        self.size = size
        self.count = 0
        self.field = [['O'] * size for _ in range(size)]
        # start_ships = [3, 2, 2, 1, 1, 1, 1]  # List of ships and their lengths
        self.busy = []
        self.ships = []
        self.start_ships = [2, 1]
        self.living_ships = []

    def __str__(self):
        res = ''
        res += f'поле {self.name_owner}: \n'
        res += '  | 1 | 2 | 3 | 4 | 5 | 6 |'
        for i, row in enumerate(self.field):
            res += f'\n{i + 1} | ' + ' | '.join(row) + ' |'
        if self.hid:
            res = res.replace('■', 'O').replace('-', 'O')
        return res

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.y][dot.x] = '■'
            self.busy.append(dot)
        self.ships.append(ship)
        self.contour(ship)
        self.living_ships.append(ship)

    def contour(self, ship, verb=True):
        near = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1)
                ]
        for dot in ship.dots:
            for dy, dx in near:
                cur = Dot(dot.y + dy, dot.x + dx)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.y][cur.x] = '-'
                    self.busy.append(cur)

    def out(self, dot):
        return not ((0 <= dot.y < self.size) and (0 <= dot.x < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException
            # return False
        # if dot in self.busy:
        #     raise BoardUserException
        for ship in self.ships:
            if ship.shooten(dot):
                ship.lives -= 1
                self.field[dot.y][dot.x] = 'X'
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    self.living_ships.remove(ship)
                    print('Корабль уничтожен!')
                    return True
                else:
                    print('Корабль ранен!')
                    return True
        self.field[dot.y][dot.x] = 'T'
        print('Мимо!')
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
    def ask(self):
        while True:
            dot = Dot(random.randrange(6), random.randrange(6))
            if (self.opponent_board.field[dot.y][dot.x] == 'X' or
                    self.opponent_board.field[dot.y][dot.x] == 'T'):
                continue
            else:
                print(f'Удар AI y, x: {dot.y + 1, dot.x + 1}')
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
            if self.opponent_board.out(dot):
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

    def random_board(self, board):
        board = board
        for length in board.start_ships:
            while True:
                a = 0
                dot = Dot(random.randrange(6), random.randrange(6))
                ship = Ship(dot, length, random.choice('hv'))
                for dot in ship.dots:
                    if board.out(dot) or board.field[dot.y][dot.x] != 'O':
                        a = 1
                if a == 1:
                    continue
                else:
                    break
            board.add_ship(ship)
        if board.name_owner == 'player':
            self.user_board = board
        else:
            self.ai_board = board
        return True

    def greet(self):
        dot = Dot(0, 0)  # ?
        ship = Ship(dot, 1)  # ?
        print(f'Вы имеете {len(self.user_board.start_ships)} кораблей, из них:')
        sum_length_ships = {'■■■': 0, '■■': 0, '■': 0}
        for length in self.user_board.start_ships:
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
        for length in self.user_board.start_ships:
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
                    if self.user_board.out(dot):
                        a = 1
                if a == 1:
                    print('Корабль вышел за границы игровой доски!!!\n'
                          'Введите через пробел y, x в диапазоне от 1 до 6:')
                    continue
                else:
                    if self.user_board.field[dot.y][dot.x] != 'O':
                        # print(self.user_board)
                        print('Место занято!!!\n'
                              'Введите через пробел y, x в диапазоне от 1 до 6:')
                        continue
                    else:
                        break
            self.user_board.add_ship(ship)
            print(self.user_board)

    def loop(self):
        victory = ''
        while True:
            while True:
                if self.user.move():
                    print(self.user_board)
                    print(self.ai_board)
                    # print(self.ai_board.living_ships)
                    if len(self.ai_board.living_ships) == 0:
                        print(self.user_board)  # ?
                        print(self.ai_board)  # ?
                        victory = 'ВЫ ПОБЕДИЛИ!!!'
                        print(victory)
                        break
                    continue
                else:
                    break
            if victory != '':
                break
            while True:
                if self.ai.move():
                    if len(self.user_board.living_ships) == 0:
                        print(self.user_board)
                        print(self.ai_board)
                        victory = 'ВЫ ПРОИГРАЛИ!!!'
                        print(victory)
                        break
                    continue
                else:
                    break
            print(self.user_board)
            print(self.ai_board)
            if victory != '':
                break

    def start(self):
        self.greet()
        print(self.user_board)
        self.random_board(self.ai_board)
        print(self.ai_board)
        self.loop()
