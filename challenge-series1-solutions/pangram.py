# pangram.py
# Pangram-checker

def pangram(string):
    """
    Checks whether a sentence is pangram or not.
    A pangram contains all letters of the alphabet.
    >>> pangram("the quick brown fox jumps over the lazy dog")
    "Congratulations. It's a pangram."
    """
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    # Input string will be compared with all alphabets.
    # If the entire string did not match with any of the alphabet, "check" value will remain zero.
    
    for i in alphabets:
        check=0
        for j in string:
            if i == j:
                check=1
        if check==0:
            return "It's not a pangram"

    return "Congratulations. It's a pangram."


string = input("Enter the pangram in small letters: ")
print(pangram(string))



