# write your solution here
def get_grades(student_info, exercise_data):
    names = {}
    with open(student_info) as student_file:
        for row in student_file:
            parts = row.strip().split(";")
            if parts[0] == "id":
                continue   
            names[int(parts[0])] = parts[1] + " " + parts[2]
        

    grades = {}
    sum_grades = {}
    with open(exercise_data) as exercise_file:
        for row in exercise_file:
            
            parts = row.strip().split(";")
            if parts[0] == "id":
                continue
            grades[int(parts[0])] = parts[1:]

        for student, grade in grades.items():
            sum_row = 0
            for sum in grade:
                sum_row += int(sum)
            sum_grades[student] = sum_row
        
    for id, name in names.items():
        if id in sum_grades:
            grade = sum_grades[id]
            print(f"{name} {grade}")

def ask_user():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        student_info = "students2.csv"
        exercise_data = "exercises2.csv"

    return student_info, exercise_data


student_info, exercise_data = ask_user()
get_grades(student_info, exercise_data)
