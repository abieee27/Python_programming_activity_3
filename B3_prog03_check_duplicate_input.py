#Abegail Q. fernandez BSCPE1-4
#B3_Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

def check_duplicate(num):
    num_str = str(num)
    unique_digits = set()
    
    for digit in num_str:
        if digit in unique_digits:
            return "Duplicate"
        unique_digits.add(digit)
    
    return "Unique"