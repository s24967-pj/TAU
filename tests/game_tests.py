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