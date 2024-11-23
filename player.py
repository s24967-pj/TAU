class Player():
    MOVES = {
            "w": (-1, 0),   # Góra
            "s": (1, 0),    # Dół
            "a": (0, -1),   # Lewo
            "d": (0, 1)     # Prawo
        }

    def __init__(self, position):
        self.position = position

    def get_move(self):
        move_input = input("Podaj ruch (w=Góra, s=Dół, a=Lewo, d=Prawo): ").strip().lower()

        if move_input in self.MOVES:
            return self.MOVES[move_input]
        else:
            print("Błędny przycisk ruchu!")
            return 0
        
    def move(self, direction):
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
