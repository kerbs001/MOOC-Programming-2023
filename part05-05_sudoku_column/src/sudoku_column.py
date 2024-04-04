# Write your solution here
def column_correct(sudoku: list, column_no: int):

    temp_list = []

    for row in sudoku:
        num = row[column_no]
        if num > 0 and num in temp_list:
            return False
        temp_list.append(num)
    return True
