# Write your solution here
def greatest_number(x, y, z):
    if x > (y + z):
        return(x)
    else:
        if x > y and x > z:
            return(x)
        elif y > z:
            return(y)
        else:
            return(z)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(12, 11, 10)
    print(greatest)