# Write your solution here
def first_word(sentence):
    word = ""
    
    for char in sentence:
        if char == " ":
            break
        word += char
    return word    

def second_word(sentence):
    word = ""
    sentence = sentence.replace(first_word(sentence) + " ", "")
    for char in sentence:
        if char == " ":
            break
        word += char
    return word

def last_word(sentence):
    word = ""
    
    for char in reversed(sentence):
        if char == " ":
            break
        word += char
    
    index = 1 
    char = 0
    final_word = ""

    for char in reversed(word):
        if index == len(word) + 1:
            break
        index += 1
        final_word += char 
    return final_word

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

