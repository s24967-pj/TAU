import unittest
import sys
import os

# Dodaj główny katalog do ścieżki systemowej (sys.path). Dzięki temu znajduje prawidłowo moduł "board"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from board import Board
from colorama import Fore, Style

class BoardTests(unittest.TestCase):

    def setUp(self):
        """Przygotowanie instancji klasy Board do testów."""
        self.board = Board(size=5)
    
    def test_smoke(self):
        self.assertTrue(True, "Smoke test zakończony niepowodzeniem!")
        print("[PASS] Smoke test zakończony pomyślnie.")

    def test_map_initialization(self):
        """Test, czy plansza jest prawidłowo zainicjowana."""
        # Sprawdzenie rozmiaru planszy
        self.assertEqual(len(self.board.map), self.board.size)
        self.assertTrue(all(len(row) == self.board.size for row in self.board.map))

        # Sprawdzenie pozycji startu i finiszu
        start_row, start_col = self.board.start
        finish_row, finish_col = self.board.finish

        self.assertEqual(self.board.map[start_row][start_col], "A")
        self.assertEqual(self.board.map[finish_row][finish_col], "B")

    def test_obstacle_generation(self):
        """Test, czy przeszkody zostały prawidłowo umieszczone na planszy."""
        # Liczymy liczbę przeszkód ("X")
        obstacle_count = sum(row.count("X") for row in self.board.map)
        # Powinna być przynajmniej jedna przeszkoda
        self.assertGreater(obstacle_count, 0)

        # Sprawdzamy, czy przeszkody nie zasłaniają startu i finiszu
        start_row, start_col = self.board.start
        finish_row, finish_col = self.board.finish
        self.assertNotEqual(self.board.map[start_row][start_col], "X")
        self.assertNotEqual(self.board.map[finish_row][finish_col], "X")

    def test_map_display(self):
        """Test metody wyświetlającej mapę."""
        try:
            Board.display(self.board.map)  # Sprawdzamy, czy metoda nie wyrzuca błędu
        except Exception as e:
            self.fail(f"Metoda wyświetlania wyrzuciła wyjątek: {e}")

    def test_update_map(self):
        """Test aktualizacji planszy z pozycją gracza."""
        player_position = (2, 2)  # Przykładowa pozycja gracza
        updated_map = self.board.update_map(player_position)

        for i, row in enumerate(updated_map):
            for j, cell in enumerate(row):
                # Sprawdzamy, czy gracz jest wyświetlany w odpowiednim miejscu
                if (i, j) == player_position:
                    self.assertEqual(cell, Fore.GREEN + "P" + Style.RESET_ALL)
                # Sprawdzamy, czy pozostałe elementy planszy są niezmienione
                elif self.board.map[i][j] == "X":
                    self.assertEqual(cell, Fore.RED + "X" + Style.RESET_ALL)
    
    def test_start_and_finish_positions(self):
        """Test, czy pozycje startu i finiszu są prawidłowe."""
        start_row, start_col = self.board.start
        finish_row, finish_col = self.board.finish

        # Pozycje startu i finiszu powinny mieścić się w obrębie planszy
        self.assertTrue(0 <= start_row < self.board.size)
        self.assertTrue(0 <= start_col < self.board.size)
        self.assertTrue(0 <= finish_row < self.board.size)
        self.assertTrue(0 <= finish_col < self.board.size)

        # Pozycje startu i finiszu nie powinny być takie same
        self.assertNotEqual(self.board.start, self.board.finish)