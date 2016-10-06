"""
   Compute factorial of the number
"""

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)


if __name__ == "__main__":
    number = int(input("Enter the number:"))
    print("Factorial of the number is:", factorial(number))
