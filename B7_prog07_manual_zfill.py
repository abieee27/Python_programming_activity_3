#Abegail Q. fernandez BSCPE1-4
#B7_Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function

text = input("Enter text: ")
width = int(input("Enter width: "))

zeros = width - len(text)
if zeros > 0:
    result = "0" * zeros + text
else:
    result = text

print(result)