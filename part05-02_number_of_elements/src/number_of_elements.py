# Write your solution here

def count_matching_elements(my_matrix: list, element: int):
    count = 0

    for list in my_matrix:
        for string in list:
            if string == element:
                count += 1
    
    return count

if __name__ == "__main__":
    m = [[1, 5, 5, 3], [2, 5, 2, 5], [0, 0, 2, 5]]
    print(count_matching_elements(m, 5))