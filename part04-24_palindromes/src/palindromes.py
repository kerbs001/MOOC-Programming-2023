# Write your solution here
def palindromes(word):
    same_word = ""
    for char in reversed(word):
        same_word += char
    
    if word == same_word:
        return True
    return False

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def main():

    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")

main()