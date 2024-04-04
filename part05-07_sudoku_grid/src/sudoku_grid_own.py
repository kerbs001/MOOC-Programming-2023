# Write your solution here

def sudoku_grid_correct(sudoku: list):

    # row check

    temp_list_row = []

    temp_list_col = []

    temp_list_grid = []

    for i in range(9):
        for j in range(9):

            #row checker
            num_row = sudoku[i][j]
            if num_row > 0 and num_row in temp_list_row:
                return False
            temp_list_row.append(num_row)

            #col checker
            num_col = sudoku[j][i]
            if num_col > 0 and num_col in temp_list_col:
                return False
            temp_list_col.append(num_col)

        temp_list_row = []

        temp_list_col = []  
    

    # grid check
    grid_row = 0
    grid_col = 0

    for grid_row in range(3):
        for grid_col in range(3):
            temp_list_grid = []  # Reset temp_list_grid for each grid check
            for i in range(3):
                for j in range(3):
                    num_grid = sudoku[grid_row * 3 + i][grid_col * 3 + j]
                    if num_grid > 0 and num_grid in temp_list_grid:
                        return False
                    temp_list_grid.append(num_grid)
    return True    
    

if __name__ == "__main__":

    sudoku = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]


    print(sudoku_grid_correct(sudoku))






    