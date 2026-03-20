#Abegail Q. fernandez BSCPE1-4
#B6_Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

text = input("enter a text: ")
all_upper = True

for ch in text:
  if 'a' <= ch <= 'z':
      all_upper = False
  break

print("Output: ", all_upper)