# Write your solution here

def length_of_longest(list):
    longest = ""
    for string in list:
        if len(string) >= len(longest):
            longest = string
    return len(longest)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)