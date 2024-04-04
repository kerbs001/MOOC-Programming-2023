# Write your solution here

def input_from_user():
    
    list_of_grades = []

    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        
        list_of_grades.extend(points.split())

        integer_list = [int(item) for item in list_of_grades]      # converts string list to integer list

    return integer_list  

def grade_calculator(grade_input):

    final_grade_list = []
    sum_points = 0

    index = 0

    while index < len(grade_input) - 1:
         
        ex_points = grade_input[index] + (grade_input[index + 1] // 10)

        sum_points += ex_points         # sum of all ex_points

        if grade_input[index] < 10:     # returns a grade of 0
            final_grade_list.append(0)
            index += 2
            continue

        #grade range 
        if ex_points > 0 and ex_points <= 14:
            final_grade_list.append(0)
        elif ex_points <= 17:
            final_grade_list.append(1)
        elif ex_points <= 20:
            final_grade_list.append(2)
        elif ex_points <= 23:
            final_grade_list.append(3)
        elif ex_points <= 27:
            final_grade_list.append(4)
        else:
            final_grade_list.append(5)

        index += 2 
        
    return sum_points, final_grade_list

def statistics(sum_points, final_grade_list):

    print("Statistics:")

    average = sum_points / len(final_grade_list) 

    print(f"Points average: {average:.1f}")

    fail_count = 0

    for j in final_grade_list:
        if j == 0:
            fail_count += 1
    
    passing = ((len(final_grade_list) - fail_count) / len(final_grade_list)) * 100

    print(f"Pass percentage: {passing:.1f}")
    print("Grade distribution:")
    grade_5 = f"    5: "
    grade_4 = f"    4: "
    grade_3 = f"    3: "
    grade_2 = f"    2: "
    grade_1 = f"    1: "
    grade_0 = f"    0: "

    for i in final_grade_list:
        if i == 5:
            grade_5 += "*"
        elif i == 4: 
            grade_4 += "*"
        elif i == 3:
            grade_3 += "*"
        elif i == 2:
            grade_2 += "*"
        elif i == 1:
            grade_1 += "*"
        else:
            grade_0 += "*"

    print(grade_5)
    print(grade_4)
    print(grade_3)
    print(grade_2)
    print(grade_1)
    print(grade_0)

def main():
    grade_input = (input_from_user())
    sum_points, final_grade_list = grade_calculator(grade_input)
    
    stats = statistics(sum_points, final_grade_list)


main()