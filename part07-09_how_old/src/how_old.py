# Write your solution here
from datetime import datetime, timedelta
day = int(input("Day of birth: "))
month = int(input("Month of birth: "))
year = int(input("Year of birth: "))

birthday = datetime(year, month, day)

age_in_days =  datetime(1999, 12, 31) - birthday 
age = age_in_days.days
if age <= 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print("You were", age, "days old on the eve of the new millennium.")