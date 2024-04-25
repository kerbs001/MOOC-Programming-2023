
def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")

            calculation = pieces[1]
            result = pieces[2]
            
            # Addition or subtraction
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
            
            #Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)

if __name__ == "__main__":
    filter_solutions()
