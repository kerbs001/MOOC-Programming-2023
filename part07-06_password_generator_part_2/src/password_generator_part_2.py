# Write your solution here
from random import sample, shuffle
import string

def generate_strong_password(length: int, num_con: bool, special_con: bool):
    password = []
    p_condition = ""
    password += sample(string.ascii_lowercase, 1)
    if num_con:
        password += sample(string.digits, 1)
        p_condition += string.digits
    if special_con:
        password += sample("!?=+-()#", 1)
        p_condition += "!?=+-()#"
    length_initial = len(password)


    password += sample(string.ascii_lowercase + p_condition, length - length_initial)
    shuffle(password)
    password = "".join(password)

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, False, False))