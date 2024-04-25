# Write your solution here
import re

def find_words(search_term: str):
    
    #database
    database = []
    with open("words.txt") as word_file:
        for line in word_file:
            word_f = line.strip()
            database.append(word_f)

            
    result = []

    if "." in search_term:
        pattern = search_term.replace(".", "[a-z]")
        regex = re.compile(pattern)
        return [word for word in database if len(word) == len(search_term) and regex.match(word)]

    #wildcard 
    elif "*" in search_term:
        word = search_term.strip("*")
        if search_term.startswith("*"):
            
            for data_word in database:            
                if data_word.endswith(word):
                    result.append(data_word)
        elif search_term.endswith("*"):
            for data_word in database:
                if data_word.startswith(word):
                    result.append(data_word)
    else:
        for data_word in database:
            if search_term == data_word:
                result.append(data_word)
    
    return(result)
            
if __name__ == "__main__":
    print(find_words("cat"))