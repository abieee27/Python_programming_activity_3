#Abegail Q. fernandez BSCPE1-4
#B6_Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

text = input("enter a string: ")
prefix = input("enter prefix to remove: ")
if text[:len(prefix)] == prefix:
   result = text[len(prefix):]
else:
  result= text
print("Output:", result)