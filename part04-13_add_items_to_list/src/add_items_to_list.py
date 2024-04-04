# Write your solution here
number_of_items = int(input("How many items: "))
count = 1
my_list = []

while count <= number_of_items:
    item = int(input(f"Item {count}: "))
    my_list.append(item)
    count += 1

print(my_list)