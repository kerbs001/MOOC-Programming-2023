# Write your solution here
import difflib


text = input("Write text: ")
compare = text.split()


with open("wordlist.txt") as word_list:
    database = []
    for line in word_list:
        word = line.strip().split(";")
        database.append(word[0])

incorrect_list = []
for word_txt in compare:
    if word_txt.lower() not in database:
        print(f"*{word_txt}*", end=" ")
        incorrect_list.append(word_txt)
        
        continue
    print(word_txt, end=" ")


print("\nsuggestions:")
for word in incorrect_list:
    matches = difflib.get_close_matches(word, database, n = 3, cutoff=0.6)
    match = ", ".join(matches)
    print(f"{word}: {match}")
        



    



             
