# Write your solution here

my_list = []
word_count = 0

while True:
    word = input("Word: ")
    if word in my_list:
        break
    my_list.append(word)
    word_count += 1

print(f"You typed in {word_count} different words")