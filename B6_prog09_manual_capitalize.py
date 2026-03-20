#Abegail Q. fernandez BSCPE1-4
#B6_Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

text = input("Enter a string: ")
print(text[:1].upper() + text[1:].lower())