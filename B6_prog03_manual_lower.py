#Abegail Q. fernandez BSCPE1-4
#B6_Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

text= input("enter a string: ")
result = ""
for ch in text:
  if 'A' <= 'Z':
      result += chr(ord(ch) + 32)
  else:
     result += ch

print("Output: ", result)