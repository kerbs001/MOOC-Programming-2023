# Copy here code of line function from previous exercise
def line(count, string):
    
    if string == "":
        print("*" * count)
    else:
        print(string[0] * count)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = height
    while i > 0:
        line(10, "#")
        i -= 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
