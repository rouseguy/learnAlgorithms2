import os
import sys

def selection_sort(filename):
    """
        Sorting numbers in a file by using selection sort
        To run, 
        $ python selection.sort.py

        Input: File name that has the numbers that are to be sorted
    """

    with open(filename) as f:
        data = f.readlines()

    data = [int(d) for d in data]

    print("Input data:")
    print(data)

    for step in range(len(data)):
        loc_smallest = step

        for location in range(step, len(data)):
                if data[loc_smallest] > data[location]:
                    loc_smallest = location

        data[step], data[loc_smallest] = data[loc_smallest], data[step]
    
    print("Sorted data:")
    print(data)

if __name__ == "__main__":
    filename = input("Enter the file to sort:")
    selection_sort(filename)
