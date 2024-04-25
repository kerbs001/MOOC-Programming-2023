# write your solution here

text = input("Write text: ")
compare = text.split()


with open("wordlist.txt") as word_list:
    database = []
    for line in word_list:
        word = line.strip().split(";")
        database.append(word[0])

for word_txt in compare:
    if word_txt.lower() not in database:
        print(f"*{word_txt}*", end=" ")
        continue
    print(word_txt, end=" ")
             
