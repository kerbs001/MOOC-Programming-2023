# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        func = "a"
        entry = input("Diary entry: ")
    elif function == 2:
        func = "r"
        print("Entries")
    elif function == 0:
        print("Bye now!")
        break
    else:
        print(ValueError)
        continue
    
    with open("diary.txt", func) as diary_file:
        if func == "a":
            diary_file.write(entry +"\n")
            print("\n")
        if func == "r":
            print(diary_file.read())
        

