#Abegail Q. fernandez BSCPE1-4
#B6_Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

text = input("Enter a string: ")
width = int(input("Enter the width to center the string: "))

total_spaces = width - len(text)

if total_spaces > 0:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    centered_text = " " * left_spaces + text + " " * right_spaces
else:
    centered_text = text

print(f"'{centered_text}'")