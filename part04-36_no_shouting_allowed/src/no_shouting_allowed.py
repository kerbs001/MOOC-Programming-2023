# Write your solution here

def no_shouting(list: list):
    no_shouting_list = []

    for string in list:
        if string.isupper():
            continue
        no_shouting_list.append(string)

    return no_shouting_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)