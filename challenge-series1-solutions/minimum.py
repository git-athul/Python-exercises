# minimum.py
# Program to find the smallest number from given list.

def min(list):
    min = list[0]
    for i in list:
        if min > i:
            min = i

    return min

# Driver function:
if __name__ == '__main__':
    list = input("Enter a list of numbers using commas: ").split(",")

    print("Smallest number from given is "+ min(list))
