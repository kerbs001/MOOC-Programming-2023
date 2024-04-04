# Write your solution here
def numbers_to_words(n):

    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n // 10 < 1: #ones
        return ones[n]
        
    elif n // 10 < 2: #teens
        return teens[n - 10]
        
    else:
        return (tens[n // 10] + ('' if n % 10 == 0 else '-' + ones[n % 10]))
    
def dict_of_numbers():
    numbers_dict = {}    
    for i in range(100):
        numbers_dict[i] = numbers_to_words(i)
    return numbers_dict