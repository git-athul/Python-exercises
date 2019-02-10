# panagram-set.py
# Panagram-checker

print("A sentence that contains all letters of the alphabet is a panagram.")

def pangram(string):
    alphabets = set(" abcdefghijklmnopqrstuvwxyz")
    str = set(string)

    # Uses set-property of only having unique elements.
    # If intersection between set-of-alphabets and set-of-input is nullset, then it's panagram. 

    if alphabets-str == set():
        print("It's pangram")
    else:
        print("It's not a pangram")

#manual-tester:
#str = "the quick brown fox jumps over the lazy dog"

str = input("Enter the pangram using small letters only: ")
pangram(str)



