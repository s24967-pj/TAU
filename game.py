from board import Board
from player import Player


class Game():
    """
    Klasa reprezentująca grę, która zarządza planszą, ruchem gracza i końcem gry.
    """

    def __init__(self, board: Board, player: Player):
        """
        Inicjalizuje nową grę.
        """
        self.board = board
        self.player = player

    def _is_game_finished(self):
        """
        Sprawdza, czy gra została zakończona.
        """
        return self.player.position == self.board.finish
    
    def is_move_correct(self, player_move):
        """
        Sprawdza, czy ruch gracza jest poprawny.
        """
        if player_move == 0:
            return False
        
        new_x = self.player.position[0] + player_move[0]
        new_y = self.player.position[1] + player_move[1]

        if 0 <= new_x < len(self.board.map) and 0 <= new_y < len(self.board.map[0]):
            return self.board.map[new_x][new_y] != "X"
        return False
    
    def display_map(self):
        """
        Wyświetla aktualną mapę z uwzględnieniem pozycji gracza i przeszkód.
        """
        self.board.display(self.board.update_map(self.player.position))

    def start_game(self):
        """
        Rozpoczyna grę, wykonując tury, aż gracz dotrze do celu.
        """
        self.display_map()

        while not self._is_game_finished():

            player_move = self.player.get_move()

            if self.is_move_correct(player_move):
                self.player.move(player_move)
                print("Wykonano ruch!")
            else:
                print("Niepoprawny ruch, spróbuj ponownie.")

            self.display_map()
        
        print("Gratulacje! Dotarłeś do celu!")


if __name__ == "__main__":
    board = Board(size=5)
    player = Player(board.start)
    game = Game(board, player)

    game.start_game()