# write your solution here

def read_matrix():
    with open("matrix.txt") as matrix:
        m = []
        for row in matrix:
            mrow = []
            numbers = row.split(",")
            for number in numbers:
                mrow.append(int(number))
            m.append(mrow)
        
        return m   
        
def matrix_max():

    max = 0
    for row in read_matrix():
        for number in row:
            if number > max:
                max = number
    return max

def matrix_sum():

    sum = 0
    for row in read_matrix():
        for number in row:
            sum += number
    return sum

def row_sums():
    row_sum = []
    
    for row in read_matrix():
        sum = 0
        for number in row:
            sum += number
        row_sum.append(sum)

    return row_sum          
                
if __name__ == "__main__":
    print(matrix_max())
    print(row_sums())
    print(matrix_sum())
