import unittest

from board import Board
from player import Player
from game import Game

class GameTests(unittest.TestCase):

    def setUp(self):
        self.board = Board(size=5)
        self.player = Player(position=self.board.start)
        self.game = Game(self.board, self.player)
    
    def test_smoke(self):
        self.assertTrue(True, "Smoke test zakończony niepowodzeniem!")
        print("[PASS] Smoke test zakończony pomyślnie.")

    def test_initial_game_state(self):
        """Test początkowego stanu gry - sprawdzenie pozycji gracza i wielkości mapy."""
        self.assertEqual(self.player.position, self.board.start)
        self.assertEqual(self.board.size, 5)

    def test_invalid_move(self):
        """Test sprawdzający, czy ruch gracza, który jest równy 0 (nieprawidłowy ruch), jest traktowany jako niepoprawny."""
        player_move = 0
        self.assertFalse(self.game.is_move_correct(player_move))
    
    def test_game_finished(self):
        """Test sprawdzający, czy gra jest zakończona, gdy gracz osiągnie pole końcowe."""
        self.player.position = self.board.finish
        self.assertTrue(self.game._is_game_finished())
 
    def test_move_out_of_bounds_up(self):
        """Test, który sprawdza, czy gracz nie może wyjść poza górną granicę planszy."""
        player_move = (-1, 0)  # Ruch do góry
        # Ustawiamy gracza na górnej krawędzi planszy
        self.player.position = (0, self.player.position[1])
        self.assertFalse(self.game.is_move_correct(player_move), "Gracz nie powinien móc wyjść poza górną granicę!")

    def test_move_out_of_bounds_down(self):
        """Test, który sprawdza, czy gracz nie może wyjść poza dolną granicę planszy."""
        player_move = (1, 0)  # Ruch w dół
        # Ustawiamy gracza na dolnej krawędzi planszy
        self.player.position = (self.board.size - 1, self.player.position[1])
        self.assertFalse(self.game.is_move_correct(player_move), "Gracz nie powinien móc wyjść poza dolną granicę!")

    def test_move_out_of_bounds_left(self):
        """Test, który sprawdza, czy gracz nie może wyjść poza lewą granicę planszy."""
        player_move = (0, -1)  # Ruch w lewo
        # Ustawiamy gracza na lewej krawędzi planszy
        self.player.position = (self.player.position[0], 0)
        self.assertFalse(self.game.is_move_correct(player_move), "Gracz nie powinien móc wyjść poza lewą granicę!")

    def test_move_out_of_bounds_right(self):
        """Test, który sprawdza, czy gracz nie może wyjść poza prawą granicę planszy."""
        player_move = (0, 1)  # Ruch w prawo
        # Ustawiamy gracza na prawej krawędzi planszy
        self.player.position = (self.player.position[0], self.board.size - 1)
        self.assertFalse(self.game.is_move_correct(player_move), "Gracz nie powinien móc wyjść poza prawą granicę!")