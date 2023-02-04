from myclass import Board, Ship, Dot, Player
from main import player_living_ships, player_ships  # player_field, computer_field


dot1 = Dot(1, 1)
ship = Ship(dot1, 3)
print('ship', ship.lives[0], ship.lives[1], ship.lives[2])
print('ships', player_ships)
player_living_ships.append(ship)
print(player_living_ships)
if dot1 in ship.lives:
    ship.lives.remove(dot1)
ship.lives.remove(ship.lives[0])
ship.lives.remove(ship.lives[0])
print(ship.lives)

if len(ship.lives) == 0:
    print('kill')
