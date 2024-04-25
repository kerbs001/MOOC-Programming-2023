# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = int(input("Choice: "))

    if choice == 1:
        fin_word = input("The word in Finnish: ")
        eng_word = input("The word in English: ")

        with open("dictionary.txt", "a") as word_file:
            word_file.write(f"{fin_word};{eng_word}\n")
        print("Dictionary entry added")

    elif choice == 2:
        search_term = input("Search term: ")
        with open("dictionary.txt") as word_file:
            for line in word_file:
                word = line.strip().split(";")
                if search_term in word[0] or search_term in word[1]:
                    print(f"{word[0]} - {word[1]}")
    
    elif choice == 3:
        print("Bye!")
        break


