# breakdown.y
# which takes a number n representing an amount of money as input
# and returns a breakdown of the amount in various denominations.

# Use 1000, 500, 100, 50, 20, 10, 5, 1 as available denominations.


def breakdown(amount):
    denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
    formatter = "{:>5} X {:5} = {:>5} ({:>5} left)"

    for i in denominations:
        count = int(amount/i)
        amount -= count*i
        print(formatter.format(i, count, i*count, amount))
    

amount = int(input("Enter the amount to breakdown: "))
breakdown(amount)
