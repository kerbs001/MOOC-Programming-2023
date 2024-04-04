# Copy here code of line function from previous exercise
def line(count, string):
    
    if string == "":
        print("*" * count)
    else:
        print(string[0] * count)
        
def square_of_hashes(size):
    # You should call function line here with proper parameters
    dim = size
    while dim > 0:
        line(size, "#")
        dim -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
