# table2.py
# Multiplication table2

def table2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==n:
                # Continues to next line
                print("{:4}".format(i*j))
            else:
                # Continues in same line
                print("{:4}".format(i*j), end=" ")


print("We are going to print the tables from 1x1 to nxn.")        
b = int(input("Enter value of n: "))
table2(b)
