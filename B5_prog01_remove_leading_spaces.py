#Abegail Q. fernandez BSCPE1-4
#B5_Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

fullname = input("enter your fullnam: ")
clean_name = fullname.lstrip()
print("output:", clean_name)