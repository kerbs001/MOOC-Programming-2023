# Write your solution here

def anagrams(word_1, word_2):
    return sorted(word_1) == sorted(word_2)

if __name__ == "__main__":
    print(anagrams("test", "set"))

#def anagrams(word_1, word_2):
#    if len(word_1) < len(word_2):
#        word_1_new = word_2
#        word_2_new = word_1

#        word_1 = word_1_new
#        word_2 = word_2_new

#    for char_1 in word_1:
#        if char_1 in word_2:
#            word_2 = word_2.replace(char_1, "", 1)
            
#        else:
#            return False
#    return True