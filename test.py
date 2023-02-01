from myclass import Board, Ship, Dot
from main import player_field


dot1, dot2 = Dot(1 - 1, 1 - 1), Dot(3 - 1, 3 - 1)
# print(dot1)
if not Board.out(dot1):
    input('Точка вне диапазона!')
ship1, ship2 = Ship(dot1, 3, 'v'), Ship(dot2, 2)
player_ships = [ship1, ship2]
player_living_ships = player_ships
dots1, dots2 = ship1.dots(), ship2.dots()

# for dot in dots1:
#    print(dot, end=' '),
# print()

player_board = Board('player', player_field, player_ships, player_living_ships, True)
player_board.add_ship(ship1.dots())
player_board.contour()
player_board.add_ship(ship2.dots())
player_board.contour()
# player_board.print_board()

dot_p = Dot(3 - 1, 1 - 1)
print(player_board.shot(dot_p))
player_board.print_board()
