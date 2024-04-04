# Write your solution here

def sum_of_positives(list):
    sum_positive = 0
    for integer in list:
        if integer > 0:
            sum_positive += integer
    
    return sum_positive

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)