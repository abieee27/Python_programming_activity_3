#Abegail Q. fernandez BSCPE1-4
#B5_Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

name = input("Enter fullname: ")
words = name.lower().split()

print("_".join(words))