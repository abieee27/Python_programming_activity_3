#Abegail Q. fernandez BSCPE1-4
#B7_Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

text = input("enter text: ")
prefix = input("enter prefix: ")
print(text[:len(prefix)]==prefix)