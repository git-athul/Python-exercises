# median.py:
# Program to find the median from given list.

def median(list):
    list  = sorted(list)
    n = len(list)

    # if even number of elements are there
    if n%2==0:
        med = (list[int(n/2)] + list[int(n/2 + 1)])/2
        
    # if odd number of elements are there
    else:
        med = list[int(n/2)]

    return med

        
# Bubble sort
def sorted(list):
    srt_list = []
    while list != []:
        srt_list.append(min(list))
        list.remove(min(list))
    return srt_list
    
    
# Driver function
if __name__ == '__main__':
    lis = input("Enter a list of numbers using commas: ").split(",")    
    print("Median from given list is "+ median(lis))


