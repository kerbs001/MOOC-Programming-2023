# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        new_dict = {}
        for fruits in new_file:
            fruits = fruits.replace("\n", "")
            parts = fruits.split(";")
            new_dict[parts[0]] = float(parts[1])
        return new_dict

if __name__ == "__main__":
    print(read_fruits())