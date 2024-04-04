# Write your solution here

def all_the_longest(list):
    longest_word = ""
    
    
    for string in list:
        if len(string) > len(longest_word):
            longest_word = string
        
    longest_list = [longest_word]

    for string in list:
        if len(longest_word) == len(string) and longest_word != string:
            longest_list.append(string)
    
    return longest_list

if __name__ == "__main__":
    my_list = ['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']

    result = all_the_longest(my_list)
    print(result) # ['eleventh']