#Abegail Q. fernandez BSCPE1-4
#B7_Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

text = input("Enter text: ")
substr = input("Enter substring: ")

count = 0
i = 0

while i <= len(text) - len(substr):
    if text[i:i+len(substr)] == substr:
        count += 1
    i += 1

print(count)