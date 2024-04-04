# Write your solution here

def no_vowels(sentence):
    vowels = "aeiou"
    new_sentence = ""

    for char in sentence:
        if char in vowels:
            continue
        new_sentence += char
    
    return new_sentence

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))