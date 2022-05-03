import unittest

from SudokuGenerator import SudokuGenerator
from solver import Solver

sudoku = SudokuGenerator()

class TestSudokuGenerator(unittest.TestCase):

    def test_size(self):
        self.assertTrue(len(sudoku.grid) == 9)
        self.assertTrue(len(sudoku.grid[0]) == 9)
        
    def test_all_numbers_in_row(self):
        for row in range(9):
            for number in range(1,10):
                self.assertTrue(number in sudoku.grid[row])

    # Fail sometimes but it's fine, just different solution
    def test_solver(self):
        sudoku.remove_random_cells(50) #remove 50 numbers
        Solver(sudoku.grid) # solve it again
        self.assertTrue(sudoku.grid == sudoku.solved) # compare to deepcopy of original
