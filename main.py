from myclass import Board, User, AI, Game


user_board = Board('player', False)
ai_board = Board('ai', False)
player = User(ai_board)
ai = AI(user_board)

game = Game(player, user_board, ai, ai_board)
game.start()
