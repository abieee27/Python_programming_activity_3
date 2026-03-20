#Abegail Q. fernandez BSCPE1-4
#B6_Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

text = input("enter text: ")
width = int(input("enter width: "))

result = text

while len(result) < width:
   result += " "
print("|" + result + "|")