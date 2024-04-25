# Write your solution here

def row_sums(my_matrix: list):
    for row in my_matrix:
        row.append(sum(row))

if __name__ == "__main__":
    matrix = row_sums([[1,3],[2,7]])
