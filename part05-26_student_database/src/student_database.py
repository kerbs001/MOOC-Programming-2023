# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []

def add_course(students: dict, name: str, course_and_grade: tuple):
    
    if course_and_grade[1] == 0:        #check if grade = 0; return if true 
        return  

    if students[name] != 0:
        for i, subject in enumerate(students[name]):              #subject is existing course; course_and_grade is new input
            if course_and_grade[0] == subject[0]:
                if course_and_grade[1] > subject[1]:
                    students[name][i] = course_and_grade
                    return
                else:
                    return
                
        students[name].append(course_and_grade)

    #if students[name] == 0, then name does not exist in the database
    

def print_student(students: dict, name: str):
    sum = 0

    if name in students:
        print(f"{name}:")
        if students[name] == []:
            print(" no completed courses")
        else:
            print(f" {len(students[name])} completed courses:")
            for subjects in students[name]:

                print(f"  {subjects[0]} {subjects[1]}")
                sum += subjects[1]
            print(f" average grade {sum/len(students[name])}")
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
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
