from myclass import Board, Ship, Dot, User, AI, Game


player_field = [['O' for x in range(6)] for y in range(6)]
computer_field = [['O' for x1 in range(6)] for y1 in range(6)]

p_dot1, p_dot2, p_dot3 = Dot(1 - 1, 1 - 1), Dot(3 - 1, 3 - 1), Dot(1 - 1, 6 - 1)
p_ship1, p_ship2, p_ship3 = Ship(p_dot1, 3, 'v'), Ship(p_dot2, 2), Ship(p_dot3, 3, 'v')
player_ships = [p_ship1, p_ship2, p_ship3]
player_living_ships = player_ships
p_dots1, p_dots2, p_dots3 = p_ship1.dots(), p_ship2.dots(), p_ship3.dots()

start_length_ships = [3, 2, 2, 1, 1, 1, 1]
# player_ships, player_living_ships = [], []
computer_ships, computer_living_ships = [], []
player_board = Board('player', player_field, player_ships, player_living_ships, True)
computer_board = Board('computer', computer_field, computer_ships, computer_living_ships, True)
player = User(player_board, computer_board)
computer = AI(computer_board, player_board)

play = Game(player, player_board, computer, computer_board)

player_board.add_ship(p_ship1.dots())
player_board.contour()
player_board.add_ship(p_ship2.dots())
player_board.contour()
player_board.add_ship(p_ship3.dots())
player_board.contour()

play.random_board(start_length_ships)

player_board.print_board()
computer_board.print_board()

while True:
    while True:
        if player.move():
            player_board.print_board()
            computer_board.print_board()
            print('Игрок ПОПАЛ!!!')
            continue
        player_board.print_board()
        computer_board.print_board()
        break
    while True:
        if computer.move():
            player_board.print_board()
            computer_board.print_board()
            print('Компьютер ПОПАЛ!!!')
            continue
        player_board.print_board()
        computer_board.print_board()
        break
