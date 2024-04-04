# Copy here code of line function from previous exercise and use it in your solution
def line(size, character):
    
    if character == "":
        print("*" * size)
    else:
        print(character[0] * size)

def shape(tri_size, tri_string, rect_size, rect_string):
    i = 1
    j = 1
    while i <= tri_size:
        line(i, tri_string)
        i += 1 
    while j <= rect_size:
        line(i-1, rect_string)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")


#        i = 0
#    j = 1
#    while i < rect_size or rect_size == 0:
#        while j <= tri_size:
#            line(j, tri_string)
#            j += 1
#        if rect_size == 0:
#            break
#        line(j-1, rect_string)
#        i += 1