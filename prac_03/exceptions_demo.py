"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When a non int type value is entered as the numerator or denominator
2. When will a ZeroDivisionError occur?
    When 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    if denominator == 0:
                print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")