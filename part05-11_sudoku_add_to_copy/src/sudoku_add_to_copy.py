# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
#    sudoku_copy = sudoku[:]
#    sudoku_copy[row_no][column_no] = number
#    return sudoku_copy


    sudoku_copy = []
    for row in range(len(sudoku)):
        temp = []
        for cell in sudoku[row]:
            temp.append(cell)
        sudoku_copy.append(temp)

    sudoku_copy[row_no][column_no] = number

    return sudoku_copy
    
    

def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print()

        for j, col in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" ", end="")

            if col != 0:
                print(col, end=" ")
            else: 
                print("_", end=" ")
        print()

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)