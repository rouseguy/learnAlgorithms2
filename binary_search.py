import os
import sys

def binary_search(file, num_to_search):
    """
    Function to compute binary search
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

    target_found = False

    while not target_found:
        if upper_bound < lower_bound:
            print("Target does not exist")
            break
       
        mid_point = lower_bound + int((upper_bound - lower_bound)/2)

        if data[mid_point] == target:
            print("Target found in the file")
            target_found = True

        if data[mid_point] < target:
            lower_bound = mid_point + 1

        elif data[mid_point] > target:
            upper_bound = mid_point - 1


if __name__ == "__main__":
    file = input("Enter file that has numbers:")
    target = input("Enter number to search in the file:")
    target = int(target)

    binary_search(file, target)
