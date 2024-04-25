# Write your solution here

def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_file, open("correct_numbers.csv", "w") as correct_file:
        for line in lottery_file:
            error = False
            word = line.replace("\n", "").split(";")
            
            #header
            header = word[0].replace("week ", "")
            try:
                number = int(header)
            except ValueError:
                error = True
            
            #list of numbers
            numbers = word[1].split(",")
            
            try:
                num_list = []
                for num in numbers:

                    #too small or large
                    if int(num) < 1 or int(num) > 39:
                        error = True
                    if int(num) in num_list:
                        error = True

                    num_list.append(int(num))

                #number count per line
                if len(num_list) == 7:
                    pass
                else:
                    error = True

                    
            except ValueError:
                error = True

            if error:
                continue
            correct_file.write(line)

if __name__ == "__main__":
    filter_incorrect()