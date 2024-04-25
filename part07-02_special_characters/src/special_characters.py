# Write your solution here
import string

def separate_characters(my_string: str):
    str1, str2, str3 = "", "", ""

    for char in my_string:
        if char in string.ascii_letters:
            str1 += char
        elif char in string.punctuation:
            str2 += char
        else:
            str3 += char
    
    return (str1, str2, str3)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])