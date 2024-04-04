# Write your solution here
my_list = []
count = 1


while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        my_list.append(count)
        count += 1
    elif choice == "r":
        my_list.pop()
        count -= 1
    else:
        print("Bye!")
        break
    
    
    
