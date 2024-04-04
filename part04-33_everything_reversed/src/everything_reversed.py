# Write your solution here

def everything_reversed(list):
    reversed_list = []
    for string in list:
        reversed_list.insert(0, string[::-1])

    return reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)