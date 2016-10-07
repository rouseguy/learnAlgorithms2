"""
   Find max number of consecutive 1s in a binary number
"""

import os
import sys
from decimal_to_binary import decimal_to_binary

def find_ones(number):
    numStr =  list(str(number))
    maxOnes = 1
    prevItem = 0
    currOnes = 0

    if number == 0:
        return 0

    else:
        for item in numStr:
            if int(item) == 1:
                currOnes = currOnes + 1
                if currOnes >= maxOnes:
                    maxOnes = currOnes
            else:
                currOnes = 0

        return maxOnes

if __name__ == "__main__":
    decimalNum = int(input("Enter the decimal number:"))
    binaryNum = decimal_to_binary(decimalNum)
    print("Binary number is:", binaryNum)
    numOnes = find_ones(binaryNum)
    print("Max Number of Consecutive 1s in the binary representation:", numOnes)


