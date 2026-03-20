#Abegail Q. fernandez BSCPE1-4
#B7_Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

text = input("Enter text: ")
islower = True
for char in text:
    if 'A' <= char <= 'Z':
        islower = False
print(islower)