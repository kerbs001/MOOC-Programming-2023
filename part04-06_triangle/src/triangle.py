# Copy here code of line function from previous exercise
def line(size, character):
    
    if character == "":
        print("*" * size)
    else:
        print(character[0] * size)

def triangle(size):
    # You should call function line here with proper parameters
    height = 1
    while height <= size:
        line(height, "#")
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
