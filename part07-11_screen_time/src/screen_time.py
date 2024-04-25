# Write your solution here
from datetime import datetime, timedelta


filename = input("Filename: ")
start_date = input("Starting date: ")
days = int(input("How many days: "))

start = datetime.strptime(start_date, "%d.%m.%Y")
end = start + timedelta(days= days - 1)

start_period  = start.strftime("%d.%m.%Y")
end_period = end.strftime("%d.%m.%Y")    


print("Please type in screen time in minutes on each day (TV computer mobile):")
with open(filename, "w") as screentime_file:
    total_minutes = 0
    result = ""
    for i in range(days):
        date = (start + timedelta(days=i)).strftime("%d.%m.%Y")
        screen_time = input(f"Screen time {date}: ")

        screen_time = screen_time.replace(" ", "/")
        for min in screen_time.split("/"):
            total_minutes += int(min)
        result += f"{date}: {screen_time}\n"
        
    
    #write results
    screentime_file.write(f"Time period: {start_period}-{end_period}\n")
    screentime_file.write(f"Total minutes: {total_minutes}\n")
    screentime_file.write(f"Average minutes: {total_minutes/days:.1f}\n")
    screentime_file.write(result)
print(f"Data stored in {filename}")