import os
import sys

def binary_search(file, num_to_search):
    """
    Function to compute binary search using recursion
    Inputs: From stdin, provide file name and the number to search
    Output: If the number is available in the file or not

    Caveat: The input file should have the numbers sorted.
    We will look into sorting the numbers later.

    """

    with open(file) as f:
        data = f.readlines()

    data = [int(num) for num in data]

    #initialize lowerbound and upperbound
    lower_bound = 0
    upper_bound = len(data) - 1

    match_found = binary_search_recursion(data, num_to_search, lower_bound, upper_bound)

    if match_found == 0:
        print("Target is not found.")
    else:
        print("Target found")



def binary_search_recursion(data, num_to_search, lower_bound, upper_bound):
    midpoint = 0
    did_it_match = 0


    if lower_bound <= upper_bound:
        midpoint = int((lower_bound + upper_bound)/2)
        
        if data[midpoint] == num_to_search:
            did_it_match = 1

        elif data[midpoint] > num_to_search:
            return binary_search_recursion(data, num_to_search, lower_bound, midpoint-1)

        else:
            return binary_search_recursion(data, num_to_search, midpoint+1, upper_bound)

    return did_it_match

if __name__ == "__main__":
    file = input("Enter file that has numbers:")
    target = input("Enter number to search in the file:")
    target = int(target)

    binary_search(file, target)
