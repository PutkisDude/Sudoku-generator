import random

grid = [[-1 for x in range(9)] for i in range(9)]

# Poistaa yhdeksikön - Tämän voisi lyhentää
def remove_square_ones(possible_numbers : list, possible_squares : list):
    tmp_list = list(possible_numbers)
    if 0 not in possible_squares:
        for i in range(0,3):
            if i in tmp_list: tmp_list.remove(i)
    if 1 not in possible_squares:
        for i in range(3,6):
            if i in tmp_list: tmp_list.remove(i)
    if 2 not in possible_squares:
        for i in range(6,9):
            if i in tmp_list: tmp_list.remove(i)
    return tmp_list


# Lisää numeron jokaiselle riville ylhäältä alaspäin
def add_number_to_lines(number):
    possible_columns = [0,1,2,3,4,5,6,7,8]
    possible_square = []

    for i in range(9):

        if not possible_square:
            possible_square = [0,1,2]
                   
        tmp_columns = remove_square_ones(possible_columns, possible_square)

        for x in range(len(grid[i])):
            if grid[i][x] != -1 and x in tmp_columns:
                tmp_columns.remove(x)

        print(tmp_columns)

        num = random.choice(tmp_columns)
        possible_columns.remove(num)
        grid[i][num] = number
        possible_square.remove(num//3)
        print(num//3)


for x in range(9):
    print(f'number : {x}')
    add_number_to_lines(x)

    for i in range(9):
        print(grid[i])
    print('next')



