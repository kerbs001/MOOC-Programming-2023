# Write your solution here
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    pool = list(range(lower + 1, upper))
    result = sorted(sample(pool, amount))

    return(result)
   
if __name__ == "__main__":
    print(lottery_numbers(6, 1, 49))
