"""
   Convert decimal number to binary number

   Input: Decimal number
   Output: Binary number

"""

import os
import sys

def decimal_to_binary(decimalNumber):
    """
        Function to convert decimal to binary
    """
    binaryNum = []
    while decimalNumber > 0:
        remainder = decimalNumber%2
        binaryNum.append(remainder)
        decimalNumber = int(decimalNumber/2)

    binNum = []
 
    for counter in range(len(binaryNum),0,-1):
        binNum.append(str(binaryNum[counter-1]))


    binNum = "".join([x for x in binNum])

    
    return int(binNum)

if __name__ == "__main__":
    number = int(input("Enter the decimal number:"))
    binary_number = decimal_to_binary(number)

    print("The binary number equivalent of ", number, " is:", binary_number)
    
