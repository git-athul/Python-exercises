# maximum.py
# Program to find the largest number from given list.

def max(list):
    max = list[0]
    for i in list:
        if max < i:
            max = i
                
    return max

# Driver-function:
if __name__ == '__main__':
    list = input("Enter a list of numbers using commas: ").split(",")
      
    print("Largest number from given is "+ max(list))
