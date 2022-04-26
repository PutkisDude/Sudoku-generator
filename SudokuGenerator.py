import random

from solver import Solver

class SudokuGenerator:
    def __init__(self):
        self.grid = [[-1 for x in range(9)] for i in range(9)]
        self.generate_sudoko()

    # Random generoi ensimmäiset laatikot
    # Laatikot vasemmasta yläkulmasta, keskeltä ja oikealta alhaalla.
    def randomize_squares(self):
        for box in range(3):
            num = box *3
            possible_numbers = [0,1,2,3,4,5,6,7,8]
            for row in range(num, num +3):
                for col in range(num, num+3):
                    random_number = random.choice(possible_numbers)
                    self.grid[row][col] = random_number
                    possible_numbers.remove(random_number)

    def generate_sudoko(self):
        self.randomize_squares()
        Solver(self.grid)
        # pass