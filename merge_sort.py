import os
import sys

def merge_sort(data):
    """
        Merge Sort Algorithm
    """

    print("Splitting:", data)

    if len(data) > 1:
        midpoint  = len(data)//2
        print("Left half:", data[:midpoint])
        print("Right half:", data[midpoint:])
        lefthalf = merge_sort(data[:midpoint])
        righthalf = merge_sort(data[midpoint:])

        i = 0
        j = 0
        k = 0
        while (i < len(lefthalf)) and (j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                data[k] = lefthalf[i]
                i = i + 1
            else:
                data[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while (i  < len(lefthalf)):
            data[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while (j < len(righthalf)):
            data[k] = righthalf[j]
            j = j + 1
            k = k + 1

    else:
        return data
    print("Merging:", data)
    return data

   
if __name__ == "__main__":
    #Get the file to sort.
    #inputFile = input("Enter file to sort:")
    inputFile = "to_sort.txt"
    #Call function to sort.
    with open(inputFile) as f:
        data = f.readlines()

    #Convert the data to integer
    data = [int(i) for i in data]

    print("Given data:")
    print(data)

    print("Sorted data:", merge_sort(data))
