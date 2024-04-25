# tee ratkaisu tänne
# wwite your solution here
def get_grades(student_info, exercise_data, exam_points, course_info):
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
    
    info_line = ""
    results_info = ""
    header = f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n"        
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
            results_info += f"{id};{name};{equiv_grade}\n"
            info_line += f"{name:<30}{sum_exer_pts[id]:<10}{exer_grade:<10}{exam_grade:<10}{final_grade:<10}{equiv_grade:<10}\n"

    with open("results.txt", "w") as results_file, open(course_info) as course_file, open("results.csv", "w") as csv_file:
        head = ""
        new_dict = {}
        for row in course_file:
            sentence = row.strip().split(":")
            new_dict[sentence[0]] = sentence[1].strip()
        

        head = f"{new_dict['name']}, {new_dict['study credits']} credits\n"
        head += ("=" *(len(head)-1))
        head += "\n"
        
        results_file.write(head)
        results_file.write(header)
        results_file.write(info_line)
    
        csv_file.write(results_info)
        

def ask_user():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
        course_info = input("Course information: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"
        course_info = "course1.txt"

    return student_info, exercise_data, exam_points, course_info


student_info, exercise_data, exam_points, course_info = ask_user()
get_grades(student_info, exercise_data, exam_points, course_info)
