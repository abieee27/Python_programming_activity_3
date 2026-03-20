#Abegail Q. fernandez BSCPE1-4
#B7_Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter text: ")
substr = input("Enter substring: ")

index = -1
for i in range(len(text) - len(substr), -1, -1):
    if text[i:i+len(substr)] == substr:
        index = i
        break

print(index)