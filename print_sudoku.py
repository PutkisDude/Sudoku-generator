from SudokuGenerator import SudokuGenerator
sudoku = SudokuGenerator()


def print_sudoku(grid):
    for row in range(9):
       print(grid[row])

print_sudoku(sudoku.grid)