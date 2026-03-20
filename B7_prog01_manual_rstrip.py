#Abegail Q. fernandez BSCPE1-4
#B7_Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

text =  input("enter your lalabs name:")
while text and text[-1] == " ": text = text[:-1]
print(text)