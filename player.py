class Player():
    """
    Klasa reprezentująca gracza w grze. Gracz ma możliwość wykonywania ruchów
    na planszy, poruszając się zgodnie z określonymi kierunkami (w, s, a, d).
    """
    
    MOVES = {
            "w": (-1, 0),   # Góra
            "s": (1, 0),    # Dół
            "a": (0, -1),   # Lewo
            "d": (0, 1)     # Prawo
        }

    def __init__(self, position):
        """
        Inicjalizuje nowego gracza z początkową pozycją.
        """
        self.position = position

    def get_move(self):
        """
        Pobiera od użytkownika ruch i zwraca odpowiadającą mu zmianę pozycji.

        Funkcja oczekuje na jeden z czterech możliwych ruchów: 'w', 's', 'a', 'd'. 
        Jeśli ruch jest niepoprawny, funkcja wypisuje komunikat o błędzie i zwraca 0.
        """
        move_input = input("Podaj ruch (w=Góra, s=Dół, a=Lewo, d=Prawo): ").strip().lower()

        if move_input in self.MOVES:
            return self.MOVES[move_input]
        else:
            print("Błędny przycisk ruchu!")
            return 0
        
    def move(self, direction):
        """
        Przesuwa gracza o określoną zmianę pozycji.
        """
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
