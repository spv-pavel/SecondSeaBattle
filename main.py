from myclass import Board, User, AI, Game


player_board = Board('игрока', False)
ai_board = Board('компьютера', True)
player = User(player_board, ai_board)
ai = AI(ai_board, player_board)

game = Game(player, player_board, ai, ai_board)
game.start()
