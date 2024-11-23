class Player():
    MOVES = {
            "w": (-1, 0),   # Góra
            "s": (1, 0),    # Dół
            "a": (0, -1),   # Lewo
            "d": (0, 1)     # Prawo
        }   

    def get_move(self):
        move_input = input("Podaj ruch (w=Góra, s=Dół, a=Lewo, d=Prawo): ").strip().lower()

        if move_input in self.MOVES:
            return self.MOVES[move_input]
        else:
            print("Nie możesz się tam ruszyć!")
            return 0