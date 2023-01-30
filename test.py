from myclass import Ship, Dot
from main import field_print, field_player

_dot = Dot(1, 2)
ship1 = Ship(_dot, 3)

_dots = ship1.dots()
print(_dots)
# print(Ship.dots(ship1))

print(field_player)

# field_print(field_player)
print(_dots[2][1])
