# Write your solution here
from random import sample
import string

def generate_password(length: int) -> str:
    password = sample(string.ascii_lowercase, length)
    password = "".join(password)
    return password

if __name__ == "__main__":
    print(generate_password(8))