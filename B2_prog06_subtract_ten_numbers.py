#Abegail Q. fernandez BSCPE1-4
#B2_Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

remainder = 0
for i in range (10):
    num = int(input(f"enter a number {i+1}: "))
    if i != 0:
        remainder = num
    else:
        remainder -= num
print("first number minus all of the remaining number is: ", remainder)