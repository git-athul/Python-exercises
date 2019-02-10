# frequency.py
# Frequency of letters:
# This program will measure the frequency of letters in input string.

def freq(string):
    s = set(string)
    count = dict()

    # Each of the element in  the string is compared through the entire string and found it's "value".
    # This value and element is updated to 'count' dictionary.
    
    for i in s:
        value=0
        for j in string:
            if i==j:
                value +=1
        count.update({i:value})
        
    print(count)


str= input("Enter a string: ")
freq(str)



