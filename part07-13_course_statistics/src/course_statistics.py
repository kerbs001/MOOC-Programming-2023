# Write your solution here
import urllib.request
import json

def retrieve_all():
    response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = response.read()
    courses = json.loads(data)

    active_courses = []
    for course in courses:
        res = ()
        if course["enabled"] == True:
            sum = 0

            for exercise in course["exercises"]:
                sum += exercise
            res += (course["fullName"], course["name"], course["year"], sum)
        
            active_courses.append(res)

    return(active_courses)

def retrieve_course(course_name: str):
    response = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = response.read()
    courses_data = json.loads(data) 

    course_dict = {}
    students = 0
    hours = 0
    exercise_count = 0 
    for course_id, course_data in courses_data.items():
        if course_data['students'] > students:
            students = course_data['students']
        hours += course_data['hour_total']  
        exercise_count += course_data['exercise_total']

        
        
        
    
    course_dict['weeks'] = len(courses_data)
    course_dict['students'] = students
    course_dict['hours'] = hours
    course_dict['hours_average'] = hours // students
    course_dict['exercises'] = exercise_count
    course_dict['exercises_average'] = exercise_count // students

    return(course_dict)
        
if __name__ == "__main__":
    retrieve_course("docker2019")