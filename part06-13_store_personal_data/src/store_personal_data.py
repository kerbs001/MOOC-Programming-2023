# Write your solution here

def store_personal_data(person: tuple):
    with open("people.csv", "a") as people_file:
        add_line = ""
        for info in person:
            if isinstance(info, float):
                add_line += str(info) + "\n"
                continue
            add_line += str(info) + ";"
        
        people_file.write(add_line)

    
    
    

if __name__ == "__main__":
    person = ("Paul Paulson", 37, 175.5)
    store_personal_data(person)