import os
import sys

if __name__ == "__main__":
    fileName = input("enter the file name that has the numbers to sort:")

    with open(fileName) as f:
        data = f.readlines()

    data = [int(d) for d in data]

    print("Given numbers:", data)

    sorted_num = sorted(data)
    print("Sorted numbers:", sorted_num)
