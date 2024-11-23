import random
from colorama import Fore, Style, init

class Board():

    def __init__(self, size: int = 5):
        init(autoreset=True)
        self.size = size
        self.board, self.start, self.finish = self._generate()
        self._generate_obstacles()
        
    def _generate(self):
        board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        start = [self.size - 1, random.randint(0, self.size - 1)]
        finish = [0, random.randint(0, self.size -1)]
        print(f"START {start}")
        print(f"FINISH {finish}")

        board[start[0]][start[1]] = "A"
        board[finish[0]][finish[1]] = "B"

        return board, start, finish
    
    def _generate_obstacles(self):
        for _ in range(self.size):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size -1)
            if self.board[x][y] == " ":
                self.board[x][y] = "X"
    
    def display(self):
        for row in self.board:
            print(" ".join(row))

    def update_board(self, player_position):
        updated_board = []       
        for i, row in enumerate(self.board):
            new_row = []
            for j, cell in enumerate(row):
                if [i, j] == player_position:
                    new_row.append(Fore.GREEN + "P" + Style.RESET_ALL)
                elif cell == "X":
                    new_row.append(Fore.RED + "X" + Style.RESET_ALL)
                else:
                    new_row.append(cell)
            updated_board.append(new_row)
        
        self.board = updated_board
