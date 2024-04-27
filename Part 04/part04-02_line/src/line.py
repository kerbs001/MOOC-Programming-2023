# Write your solution here
def line(count, string):
    if string == "":
        print("*" * count)
    else:
        print(string[0] * count)
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")