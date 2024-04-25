# Write your solution here
import string
from random import shuffle

def words(n: int, beginning: str):
    with open("words.txt") as f:
        my_list = []
        ns = 0
        words = f.read().split()
        shuffle(words)

        for word in words:
            if word.startswith(beginning):
                my_list.append(word)
                ns += 1
            if ns == n:
                break
        
        if ns < n:
            raise ValueError
        
        return(my_list)

    
        

            
if __name__ == "__main__":
    word_list = words(2, "car")
    n = 0
    for word in word_list:
        n += 1 
        print(word)
    print(n)