

class Solver:

    def __init__(self, grid : list):
        self.grid = grid
        self.solve()
 
    # Etsii seuraavan tyhjän ruudun
    def find_empty_cell(self, location) -> bool:
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == -1:
                    location[0] = row
                    location[1] = col
                    return True
        return False # ei tyhjiä ruutuja


    def valid_cell(self, row, col, number):
        # Tarkistaa onko numero jo rivillä
        if number in self.grid[row]:
            return False

        #Tarkistaa onko numero sarakkeessa
        for i in range(9):
            if number == self.grid[i][col]:
                return False

        #Tarkistaa onko numero laatikossa / yhdeksikössä
        box_row = row //3 *3 # palauttaa kokonaisluvun: 0 | 3 | 6
        box_col = col //3 *3
        
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if number == self.grid[i][j]:
                    return False
        
        return True # Jos numero kelpaa


    def solve(self) -> bool:
            # Pitää muistissa missä mennään
            l = [0,0]

            if (not self.find_empty_cell(l)):
                return True

            row = l[0]
            col = l[1]

            for number in range(9):

                if(self.valid_cell(row, col, number)):
                    self.grid[row][col] = number

                    if(self.solve()):
                        return True

                    self.grid[row][col] = -1 # palauttaa ruudun tyhjäksi epäonnistuessa


            return False # Jos sudokua ei voi ratkaista


            