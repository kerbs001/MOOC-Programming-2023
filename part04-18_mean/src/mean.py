# Write your solution here
def mean(my_list):
    sum = 0
    
    for char in my_list:
        sum += char
        char += 1 
    
    return round(sum / len(my_list), 1)

    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)