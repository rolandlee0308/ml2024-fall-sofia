"""
The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
"""

__author__ = "Roland Lee"

userInput = input("Please enter input N (positive integer) :")
print(f"You entered: {userInput}")

userList = []
for i in range(int(userInput)):
    number = input("Please enter a number :")
    print(f"You entered: {number}")
    userList.append(number)

endInput = input("Enter a number that is in the list :")
try:
    index = userList.index(endInput)
    print(f"{index}")
except ValueError:
    print(f"-1")
