def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

def column_correct(sudoku: list, column_no: int):

    temp_list = []

    for row in sudoku:
        num = row[column_no]
        if num > 0 and num in temp_list:
            return False
        temp_list.append(num)
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):

    temp_list = []
    for i in range(3):
        for j in range(3):
            num = sudoku[row_no + i][column_no + j]
            if num > 0 and num in temp_list:
                return False
            temp_list.append(num)
    
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
    
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
    
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
            
    return True