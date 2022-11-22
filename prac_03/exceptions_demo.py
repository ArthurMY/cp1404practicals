"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ANS: When the input is not the integer number.
2. When will a ZeroDivisionError occur?
ANS: When the denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ANS: Add a 'while' loop under the input lines. The 'while' loop will do the ZeroDiveison checking.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")


print("Finished.")
