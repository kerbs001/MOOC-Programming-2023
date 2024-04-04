# Write your solution here
def shortest(list):
    short = "+++++++++++++++" #initializer
    for string in list:
        if len(string) < len(short):
            short = string
    
    return short


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)