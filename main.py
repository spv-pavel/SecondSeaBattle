from myclass import Board, User, AI, Game


player_field = [['O' for x in range(6)] for y in range(6)]
ai_field = [['O' for x1 in range(6)] for y1 in range(6)]

player_ships, player_living_ships = [], []
ai_ships, computer_living_ships = [], []

player_board = Board('player', player_field, player_ships, player_living_ships, True)
ai_board = Board('ai', ai_field, ai_ships, computer_living_ships, True)
player = User(player_board, ai_board)
ai = AI(ai_board, player_board)

game = Game(player, player_board, ai, ai_board)
game.start()
