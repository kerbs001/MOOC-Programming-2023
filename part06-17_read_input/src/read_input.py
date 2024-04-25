# Write your solution here

def read_input(statement, lower_limit, upper_limit):
    while True:
        try:
            num = int(input(statement))
            if num > lower_limit and num < upper_limit:
                return(num)
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        except ValueError:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
            continue

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)