#Abegail Q. fernandez BSCPE1-4
#B6_Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

text = input("enter a text: ")
suffix = input("enter a ending to check: ")

if text[len(text)-len(suffix):] == suffix:
    result = True
else:
     result = False
print("Output:", result)

