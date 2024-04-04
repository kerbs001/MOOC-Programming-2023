# Write your solution here

pos_integer = int(input("Please type in a positive integer: "))

for i in range(-pos_integer, pos_integer+1):
    if i == 0:
        continue
    print(i)