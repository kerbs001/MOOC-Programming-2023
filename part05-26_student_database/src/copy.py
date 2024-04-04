# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []

def add_course(students: dict, name: str, course_and_grade: tuple):
    
    if course_and_grade[1] == 0:
        return

    if students[name] != 0:
        for subject in students[name]:
            if course_and_grade[0] == subject[0]:
                print('hello')
                if course_and_grade[1] > subject[1]:
                    subject[1] = course_and_grade[1]
                    return
                else:
                    return
                
        students[name].append(course_and_grade)
    

def print_student(students: dict, name: str):
    sum = 0

    if name in students:
        print(f"{name}:")
        if students[name] == []:
            print(" no completed courses")
        else:
            print(f"{len(students[name][1])} completed courses:")
            for subjects in students[name]:

                print(f"  {subjects[0]} {subjects[1]}")
                sum += subjects[1]
            print(f"average grade {sum/len(students[name])}")
    else:
        print(f"{name}: no such person in the database")

def summary(students: dict):
    print(f"students {len(students)}")
    max = 0
    max_name = ""
    for student in students:
        if len(students[student]) > max:
            max = len(students[student])
            max_name = student
    print(f"most courses completed {max} {max_name}")

    max_average = 0
    max_name = ""
    for student, courses in students.items():
        sum = 0
        for course, grade in courses:
            sum += grade
        average = sum / len(courses)
        if average > max_average:
            max_average = average
            max_name = student

    print(f"best average grade {max_average} {max_name}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
