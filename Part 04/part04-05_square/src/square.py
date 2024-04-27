# Copy here code of line function from previous exercise
def line(count, string):
    
    if string == "":
        print("*" * count)
    else:
        print(string[0] * count)

def square(size, character):
    # You should call function line here with proper parameters
    i = size
    while i > 0:
        line(size, character)
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")