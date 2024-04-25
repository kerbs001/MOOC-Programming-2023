# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    fraction_list = []
    for i in range(amount):
        fraction_list.append(Fraction(1, amount))
        
    return fraction_list

if __name__ == "__main__":
    print(fractionate(3))


