grade_input = 25, 20, 35, 40

def grade_calculator(grade_input):

    final_grade_list = []
    sum_points = 0

    index = 0

    while index < len(grade_input):
         
        ex_points = grade_input[index] + (grade_input[index + 1] // 10)

        sum_points += ex_points         # sum of all ex_points

        if grade_input[index] < 10:     # returns a grade of 0
            final_grade_list.append(0)
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
        
    print(final_grade_list)