# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as student_file:
        data = student_file.read()
    
        students = json.loads(data)

        for student in students:
            print(f"{student['name']} {student['age']} years ({(', '.join(student['hobbies']))})")

if __name__ == "__main__":
    print_persons("src/file1.json")
