# Write your solution here

def most_common_character(string):
    highest = 0
    highest_count = ""

    for char in string:
        if string.count(char) > highest:
            highest = string.count(char)
            highest_count = char

    return highest_count

if __name__ == "__main__":
    first_string = "bbbaaa"
    print(most_common_character(first_string))
        
