import os
import sys

def linear_search(file, target):
    """
        Function to do linear search

        To run: At the command prompt:
            $ python linear_search.py numbers.txt 5

        Notes about the arguments:
        linear_search.py -> This program file
        numbers.txt -> A file with numbers. 
        5 -> The number to search

    """

    # Read the file

    with open(file) as f:
        data = f.readlines()

    # Convert the data into integers
    data = [int(num) for num in data]

    # pick each element from data and match it with target. 
    # If it matches, return with match found message. Else print match not found.

    for num in data:
        if num == target:
            print("Match found.")
            return None

    print("Match not found.")

if __name__ == "__main__":
    # filename = sys.argv[1]
    # number_to_search = int(sys.argv[2])
    filename = input("Enter file name that has the numbers:")
    number_to_search = input("Enter the number to search in the file:")
    number_to_search = int(number_to_search)
    linear_search(filename, number_to_search)

