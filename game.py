from board import Board
from player import Player


class Game():
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

if __name__ == "__main__":
    board = Board()
    player = Player()
    game = Game(board, player)

    board.update_board(board.start)
    board.display()