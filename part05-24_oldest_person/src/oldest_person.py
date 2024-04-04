# Write your solution here
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person

    return oldest[0]

if __name__ == "__main__":
    people = [('Jacob', 2016), ('Harry', 2019), ('Oliver', 2012), ('Wendy', 2013), ('Jane Doe', 2020)]

    print(oldest_person(people))