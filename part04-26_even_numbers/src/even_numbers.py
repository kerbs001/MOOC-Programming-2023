# Write your solution here

# Write your solution here

def even_numbers(list):
    new_list = []

    for integer in list:
        if integer % 2 == 0:
            new_list.append(integer)
    
    return new_list

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    new_list = even_numbers(list)
    print("original", list)
    print("new", new_list)