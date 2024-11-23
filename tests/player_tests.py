import unittest

from unittest.mock import patch
# Używamy "patch", aby zastąpić funkcję "input" wbudowaną w Pythona.
# Funkcja input() będzie teraz zwracać wartość zgodnie z przygotowanym "@patch" bez potrzeby rzeczywistego
# wprowadzania danych przez użytkownika.
from player import Player

class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.player = Player(position=(2, 2))

    def test_initial_position(self):
        """Test sprawdzający początkową pozycję gracza."""
        self.assertEqual(self.player.position, (2, 2))

    @patch('builtins.input', return_value='w')
    # "mock_input" to zamockowana wersja funkcji "input", która działa tak, jakby była normalną funkcją,
    # ale zamiast czekać na rzeczywiste dane wejściowe od użytkownika, natychmiast zwraca wartość określoną w "patch"
    def test_get_move_up(self, mock_input):
        """Test sprawdzający metodę get_move() - ruch w górę."""
        # Funkcja input() będzie teraz zwracać wartość 'w' bez potrzeby rzeczywistego
        # wprowadzania danych przez użytkownika.
        move = self.player.get_move()
        self.assertEqual(move, (-1, 0))

    @patch('builtins.input', return_value='s')
    def test_get_move_down(self, mock_input):
        """Test sprawdzający metodę get_move() - ruch w dół."""
        # Podobnie jak wcześniej, zastępujemy funkcję input() tak, aby zwracała 's'.
        move = self.player.get_move()
        self.assertEqual(move, (1, 0))

    @patch('builtins.input', return_value='a')
    def test_get_move_left(self, mock_input):
        """Test sprawdzający metodę get_move() - ruch w lewo."""
        # Zastępujemy input() na 'a', który oznacza ruch w lewo.
        move = self.player.get_move()
        self.assertEqual(move, (0, -1))

    @patch('builtins.input', return_value='d')
    def test_get_move_right(self, mock_input):
        """Test sprawdzający metodę get_move() - ruch w prawo."""
        # Zastępujemy input() na 'd', który oznacza ruch w prawo.
        move = self.player.get_move()
        self.assertEqual(move, (0, 1))

    @patch('builtins.input', return_value='x')
    def test_invalid_move(self, mock_input):
        """Test sprawdzający metodę get_move() - niepoprawny ruch."""
        # Zastępujemy input() na 'x', który nie jest poprawnym ruchem w żadnym kierunku.
        move = self.player.get_move()
        self.assertEqual(move, 0)  # Niepoprawny ruch powinien zwrócić 0

    def test_move_up(self):
        """Test sprawdzający metodę move() - ruch w górę."""
        self.player.move((-1, 0))
        self.assertEqual(self.player.position, (1, 2))  # Ruch w górę zmienia pozycję na (1, 2)

    def test_move_down(self):
        """Test sprawdzający metodę move() - ruch w dół."""
        self.player.move((1, 0))
        self.assertEqual(self.player.position, (3, 2))  # Ruch w dół zmienia pozycję na (3, 2)

    def test_move_left(self):
        """Test sprawdzający metodę move() - ruch w lewo."""
        self.player.move((0, -1))
        self.assertEqual(self.player.position, (2, 1))  # Ruch w lewo zmienia pozycję na (2, 1)

    def test_move_right(self):
        """Test sprawdzający metodę move() - ruch w prawo."""
        self.player.move((0, 1))
        self.assertEqual(self.player.position, (2, 3))  # Ruch w prawo zmienia pozycję na (2, 3)