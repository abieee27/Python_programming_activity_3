#Abegail Q. fernandez BSCPE1-4
#B2_Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []
for i in range (1, 11):
    num = int(input(f"enter number {i}: "))
    if num in range (1,11): 
        numbers.append(num)

for num in numbers:
    if numbers.count(num) == 1:
        print(num)