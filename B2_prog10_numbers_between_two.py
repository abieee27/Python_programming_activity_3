#Abegail Q. fernandez BSCPE1-4
#B2_Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
for number in range (num1, num2 + 1):
    print(number)