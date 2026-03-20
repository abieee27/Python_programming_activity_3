#Abegail Q. fernandez BSCPE1-4
#B7_Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

text = input("enter text: ")
suffix = input("enter suffix: ")
print(text[:-len(suffix)] if text[-len(suffix):] == suffix else text)