from myclass import Board, Ship, Dot, User, AI


player_field = [['0' for x in range(6)] for y in range(6)]
computer_field = [['0' for x1 in range(6)] for y1 in range(6)]

p_dot1, p_dot2 = Dot(1 - 1, 1 - 1), Dot(3 - 1, 3 - 1)
c_dot1, c_dot2 = Dot(2 - 1, 2 - 1), Dot(4 - 1, 4 - 1)
if not Board.out(p_dot1):
    input('Точка вне диапазона!')
p_ship1, p_ship2 = Ship(p_dot1, 3, 'v'), Ship(p_dot2, 2)
c_ship1, c_ship2 = Ship(c_dot1, 3, 'v'), Ship(c_dot2, 2)
player_ships = [p_ship1, p_ship2]
computer_ships = [c_ship1, c_ship2]
player_living_ships = player_ships
computer_living_ships = computer_ships
p_dots1, p_dots2 = p_ship1.dots(), p_ship2.dots()
c_dots1, c_dots2 = c_ship1.dots(), c_ship2.dots()
# for dot in dots1:
#    print(dot, end=' '),
# print()

player_board = Board('player', player_field, player_ships, player_living_ships, True)
computer_board = Board('computer', computer_field, computer_ships, computer_living_ships, True)
player_board.add_ship(p_ship1.dots())
player_board.contour()
player_board.add_ship(p_ship2.dots())
player_board.contour()
computer_board.add_ship(c_ship1.dots())
computer_board.contour()
computer_board.add_ship(c_ship2.dots())
computer_board.contour()
player_board.print_board()
computer_board.print_board()

player = User(player_board, computer_board)
computer = AI(computer_board, player_board)
while True:
    while True:
        if player.move():
            player_board.print_board()
            computer_board.print_board()
            continue
        player_board.print_board()
        computer_board.print_board()
        break
    while True:
        if computer.move():
            player_board.print_board()
            computer_board.print_board()
            print('ПОПАЛ')
            continue
        player_board.print_board()
        computer_board.print_board()
        break

