# Write your solution here

def list_sum(a, b):
    new_list = []
    i = 0
    while i < len(a):
        new_list.append(a[i] + b[i]) 
        i += 1
    return new_list
    
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]