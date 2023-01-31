from myclass import Board, Ship, Dot
from main import print_field, player_field


dot1, dot2 = Dot(1, 2), Dot(3, 3)
ship1, ship2 = Ship(dot1, 3), Ship(dot2, 2)
player_ships = [ship1, ship2]
player_living_ships = player_ships
dots1, dots2 = ship1.dots(), ship2.dots()
print(dots1)
print(dots2)
# print(Ship.dots(ship1))
print(dot1.y, dot1.x)

player_board = Board(player_field, player_ships, player_living_ships, True)
player_board.add_ship(ship1)

print_field(player_field)
# print(_dots[2][1])
