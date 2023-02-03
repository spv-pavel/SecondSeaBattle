from myclass import Board, User, AI, Game


player_field = [['O' for x in range(6)] for y in range(6)]
computer_field = [['O' for x1 in range(6)] for y1 in range(6)]

start_length_ships = [3, 2, 2, 1, 1, 1, 1]
# start_length_ships = [3, 2]
player_ships, player_living_ships = [], []
computer_ships, computer_living_ships = [], []
player_board = Board('player', player_field, player_ships, player_living_ships, True)
computer_board = Board('computer', computer_field, computer_ships, computer_living_ships, True)
player = User(player_board, computer_board)
computer = AI(computer_board, player_board)

game = Game(player, player_board, computer, computer_board)

# game.greet(start_length_ships)
game.random_board(player_board, start_length_ships)
game.random_board(computer_board, start_length_ships)
player_board.print_board()
computer_board.print_board()

'''
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
'''