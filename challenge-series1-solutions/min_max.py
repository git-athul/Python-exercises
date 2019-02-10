# min_max.py
# Program to find Maximum and minimum from given list.

import maximum
import minimum


list = input("Enter a list of numbers using commas: ").split(",")
       
print("Largest number from given is "+ maximum.max(list))
print("Smallest number from given is "+ minimum.min(list))






