from myclass import Board, User, AI, Game


user_board = Board('player', False)
ai_board = Board('ai', True)
player = User(user_board, ai_board)
ai = AI(ai_board, user_board)

game = Game(player, user_board, ai, ai_board)
game.start()
