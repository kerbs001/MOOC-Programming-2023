# Write your solution here


layers = int(input("Layers: "))

side_length = 2 * layers - 1

for i in range(side_length):
    row = ''
    for j in range(side_length):
        distance_to_center = min(i, j, side_length - i - 1, side_length - j - 1)
        letter = chr(ord('A') + layers - distance_to_center - 1)
        row += letter
    print(row)

