# Write your solution here
def spruce(char):
    height = 1
    space = char - 1 
    print("a spruce!")
    while (height / 2) <= char:                      
        print(f"{' ' * space + '*' * height}")
        height += 2
        space -= 1
    
    print(f"{' ' * (char - 1) + '*'}")



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)