# Write your solution here
from random import randint

def roll(die: str):
    roll_dict = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}
    return roll_dict[die][randint(0, 5)]

def play(die1: str, die2: str, times: int):
    win1 = 0
    win2 = 0
    tie = 0
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if result1 > result2:
            win1 += 1
        elif result1 < result2:
            win2 += 1
        else:
            tie += 1
        
    return (win1, win2, tie)


if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")