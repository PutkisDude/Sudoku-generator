from SudokuGenerator import SudokuGenerator
import time

sudoku = SudokuGenerator()

start = time.perf_counter()
for i in range(100):
    sudoku.generate_sudoko()

end = time.perf_counter()

print(end - start)