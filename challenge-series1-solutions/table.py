# table.py:
# Multiplication table

def table(m,n):
    for i in range(1,n+1):
        print(f"{m} X {i} = {m*i}")


        
print("We are going to print the m times tables from 1 to n.")        
a = int(input("Enter value of m: "))
b = int(input("Enter value of n: "))

table(a,b)
