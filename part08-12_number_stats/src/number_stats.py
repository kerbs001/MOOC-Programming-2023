# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.number_list = []

    def add_number(self, number: int):
        self.number_list.append(number)
        self.numbers += number

    def count_numbers(self):
        return(len(self.number_list))
        pass

    def get_sum(self):
        if self.numbers != 0:
            return(sum(self.number_list))
        else:
            return(0)

    def average(self):
        if self.numbers != 0:
            ave = sum(self.number_list) / len(self.number_list)
            return(ave)
        else:
            return(0)
    

def main():
    even_numbers = NumberStats()
    odd_numbers = NumberStats()
    number = NumberStats()
    while True:
        integer = int(input("Please type in integer numbers: "))
        if integer == -1:
            break
        
        if integer % 2 == 0:
            even_numbers.add_number(integer)
        else:
            odd_numbers.add_number(integer)

        number.add_number(integer)

    
    print(f"Sum of numbers: {number.get_sum()}")
    print(f"Mean of numbers: {number.average()}")
    print(f"Sum of even numbers: {even_numbers.get_sum()}")
    print(f"Sum of odd numbers: {odd_numbers.get_sum()}")

main()