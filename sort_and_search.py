"""
    Enter the file name that has the numbers and a number that has to be searched.
    Sort using merge sort.
    Find using binary search.
    Leverage existing code
"""

import os
import sys
from binary_search import binary_search
from merge_sort import merge_sort

if __name__ == "__main__":
    fileName = input("Enter file name that has the numbers:")
    numSearch = input("Enter the number that has to be searched:")
    numSearch = int(numSearch)

    with open(fileName) as f:
        data = f.readlines()

    data = [int(d) for d in data]

    sorted_data = merge_sort(data)
    binary_search(sorted_data, numSearch)
