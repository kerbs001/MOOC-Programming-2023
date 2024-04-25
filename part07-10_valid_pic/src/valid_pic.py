# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    result = True
    if len(pic) != 11:
        return False

    century_marker = {"+": 1800, "-": 1900, "A": 2000}

    #ddmmyy checker
    year = century_marker[pic[6]] + int(pic[4:6])
    month = int(pic[2:4])
    date = int(pic[:2])
    try:
        datetime(year, month, date)
    except ValueError:
        result = False

    control_num = int(pic[0:6] + pic[7:10]) % 31

    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if control_string[control_num] == pic[10]:
        pass
    else:
        result = False
    
    return result
    
    

if __name__ == "__main__":
    pic = "120488+246L"
    print(is_it_valid(pic))