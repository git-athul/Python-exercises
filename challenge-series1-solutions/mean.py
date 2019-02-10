# mean.py:
# Program to find Mean from given list.

def mean(list):
    mean = 0
    count = 0
    for i in list:
        count += 1
        mean += float(i)
    
    mean = mean/count
    return mean

# Driver-function:
if __name__ == '__main__':
    list = input("Enter a list of numbers using commas: ").split(",")

    print("Mean is ", mean(list))



    
