# Write your solution here

sign = input("Whom should I sign this to: ")
file_save = input("Where shall I save it: ")

with open(file_save, 'w') as new_file:
    new_file.write (f"Hi {sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")

print(new_file)