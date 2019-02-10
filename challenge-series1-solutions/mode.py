# mode.py:
# Program to find the mode from given list of numbers.

def mode(list):
    set_list = set(list)
    count = dict()
    mode_result = []

    # Set of the list gives us unique elements in list
    # Elements in set is then compared through to list.
    # Each time element is matched with the list it's "value" icrease by 1.
    # This value and element is updated to 'count' dictionary.
    
    for i in set_list:
        value=0
        for j in list:
            if i==j:
                value +=1
        count.update({i:value})

    # A dictionary has key:value pair. Here keys are elements and values are count of elements.    
    # Keys that have maximum values are modes. These values are appended to a list.
    # When no number occurs more than once in a data set, there is no mode.
    
    if max(count.values()) == 1:
        return "There is no mode"
    else:
        for key, value in count.items():
            if max(count.values()) == value:
                mode_result.append(key)
        
    return mode_result



# Driver function
if __name__ == '__main__':
    lis = input("Enter a list of numbers using commas: ").split(",")    
    print("Result: ", sorted(mode(lis)))

#manual tester:    
#lis=[1,1,2,2,3,3,4,5]    



