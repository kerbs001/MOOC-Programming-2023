# wwite your solution here
def get_grades(student_info, exercise_data, exam_points):
    names = {}
    with open(student_info) as student_file:
        for row in student_file:
            parts = row.strip().split(";")
            if parts[0] == "id":
                continue   
            names[int(parts[0])] = parts[1] + " " + parts[2]
        

    grades = {}
    sum_exer_pts = {}
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
            sum_exer_pts[student] = sum_row
    
    exam_pts = {}
    sum_exam_pts = {}
    with open(exam_points) as exam_file:
        for row in exam_file:
            parts = row.strip().split(";")
            if parts[0] == "id":
                continue
            exam_pts[int(parts[0])] = parts[1:]
        
        for student, pts in exam_pts.items():
            sum = 0
            for pt in pts:
                sum += int(pt)
            sum_exam_pts[student] = sum
        

        
    for id, name in names.items():
        if id in sum_exer_pts:
            exer_grade = sum_exer_pts[id] // 4
            exam_grade = sum_exam_pts[id]
            final_grade =  exer_grade + exam_grade
            if final_grade <= 14:
                equiv_grade = 0
            elif final_grade <= 17:
                equiv_grade = 1
            elif final_grade <= 20:
                equiv_grade = 2
            elif final_grade <= 23:
                equiv_grade = 3
            elif final_grade <= 27:
                equiv_grade = 4
            else:
                equiv_grade = 5
            print(f"{name} {equiv_grade}")

    

def ask_user():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"

    return student_info, exercise_data, exam_points


student_info, exercise_data, exam_points = ask_user()
get_grades(student_info, exercise_data, exam_points)
