from myclass import Board, User, AI, Game


player_field = [['O' for x in range(6)] for y in range(6)]
computer_field = [['O' for x1 in range(6)] for y1 in range(6)]

# start_length_ships = [3, 2, 2, 1, 1, 1, 1]
start_length_ships = [2, 3]  # может сделать через глобальную переменную?
player_ships, player_living_ships = [], []
computer_ships, computer_living_ships = [], []

player_board = Board('player', player_field, player_ships, player_living_ships, True)
computer_board = Board('computer', computer_field, computer_ships, computer_living_ships, True)
player = User(player_board, computer_board)
computer = AI(computer_board, player_board)

game = Game(player, player_board, computer, computer_board)
game.start(start_length_ships)

# game.greet(start_length_ships)
# game.random_board(player_board, start_length_ships)
# game.random_board(computer_board, start_length_ships)
# player_board.print_board()
# computer_board.print_board()
# game.loop()
