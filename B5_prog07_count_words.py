#Abegail Q. fernandez BSCPE1-4
#B5_Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

text = input("Enter sentence: ")
words = text.split()
print(len(words))