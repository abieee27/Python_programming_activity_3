#Abegail Q. fernandez BSCPE1-4
#B6_Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# Prog01: Remove leading spaces without using lstrip()

fullname = input("Enter your fullname: ")

i = 0 

while i < len(fullname) and fullname[i] == ' ':
    i += 1

clean_name = fullname[i:]
print("Output:", clean_name)