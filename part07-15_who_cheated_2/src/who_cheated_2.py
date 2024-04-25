# Write your solution here
from datetime import datetime, timedelta

def cheaters():
    # Read start times
    start_times = {}
    with open("start_times.csv", 'r') as file:
        for line in file:
            name, start_time_str = line.strip().split(';')
            start_times[name] = datetime.strptime(start_time_str, '%H:%M')
    

    # Read submissions and check for cheaters
    cheaters_list = set()
    with open("submissions.csv", 'r') as file:
        for line in file:
            name, _, _, submit_time_str = line.strip().split(';')
            if name in start_times:
                submit_time = datetime.strptime(submit_time_str, '%H:%M')
                time_diff = submit_time - start_times[name]

                if time_diff.total_seconds() > 3 * 3600:  # Check if time difference is over 3 hours
                    cheaters_list.add(name)

    return sorted(list(cheaters_list))


def final_points():
    # Read start times
    start_times = {}
    with open("start_times.csv", 'r') as file:
        for line in file:
            name, start_time_str = line.strip().split(';')
            start_times[name] = datetime.strptime(start_time_str, '%H:%M')

    # Initialize a dictionary to store the final points
    final_points_dict = {}

    # Read submissions
    with open("submissions.csv", 'r') as file:
        for line in file:
            name, task, points_str, submit_time_str = line.strip().split(';')
            task = int(task)
            points = int(points_str)
            submit_time = datetime.strptime(submit_time_str, '%H:%M')

            # Check if submission is within 3 hours and has higher points
            if name not in final_points_dict:
                final_points_dict[name] = {}
            if task not in final_points_dict[name] or final_points_dict[name][task] < points:
                time_diff = submit_time - start_times.get(name, datetime.min)
                if time_diff.total_seconds() <= 3 * 3600:
                    final_points_dict[name][task] = points

    # Calculate total points for each student
    total_points_dict = {}
    for name, submissions in final_points_dict.items():
        total_points_dict[name] = sum(submissions.values())
        print(submissions.values())

    print(total_points_dict)

    return total_points_dict

if __name__ == "__main__":

    print(final_points())