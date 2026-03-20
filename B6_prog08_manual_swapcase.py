#Abegail Q. fernandez BSCPE1-4
#B6_Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

text = input("enter a string: ")
swapped_text = ""

for char in text:
    if char.isupper():
        swapped_text += char.lower()
    elif char.islower():
        swapped_text += char.upper()  
    else:
        swapped_text += char           

print(swapped_text)