#Abegail Q. fernandez BSCPE1-4
#B5_Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

name = input("Enter fullname: ")
words = name.split()

result = ""
for word in words:
    result += word.capitalize()

print(result)