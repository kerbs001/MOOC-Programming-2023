# Write your solution here

def search(persons):
    name = input("name: ")
    if name not in persons:
        print("no number")
    else:
        for value in persons[name]:
            print(value)

def add(persons):
    name = input("name: ")
    number = input("number: ")
    if name not in persons:
        persons[name] = []
    persons[name].append(number)
    print("ok!")

def main():
    persons = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            search(persons)
        elif command == 2: 
            add(persons)
        elif command == 3: 
            break
    print("quitting...")        

main()