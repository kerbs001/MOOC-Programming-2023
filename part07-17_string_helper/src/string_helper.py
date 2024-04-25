# Write your solution here
import string

def change_case(orig_string: str):
    new_string = ""
    for char in orig_string:
        print(char)
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    
    return(new_string)

def split_in_half(orig_string: str):
    return (orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:])

def remove_special_characters(orig_string: str):

    for char in orig_string:
        if char not in (string.ascii_letters + string.digits + string.whitespace):
            orig_string = orig_string.replace(char, "")
    
    return(orig_string)

if __name__ == "__main__":
    orig_string = input("Please type in a string: ")
    print(change_case(orig_string))