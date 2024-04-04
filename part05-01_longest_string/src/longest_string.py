# Write your solution here


def longest(strings: list):

    longest_word = ""
    for word in strings:
        if len(longest_word) < len(word):
            longest_word = word
    

    return longest_word

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))