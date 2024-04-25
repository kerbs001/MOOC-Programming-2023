# Write your solution here

def new_person(name: str, age: int):
    if name == "":
        raise ValueError
    elif age < 0:
        raise ValueError
    elif len(name) > 40:
        raise ValueError
    elif age > 150:
        raise ValueError
    else:
        count = name.split()
        if len(count) < 2:
            raise ValueError
        return(name, age)
    
if __name__ == "__main__":
    print('Andrew', 32)
