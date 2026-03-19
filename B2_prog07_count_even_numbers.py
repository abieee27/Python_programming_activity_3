#Abegail Q. fernandez BSCPE1-4
#B2_Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

even = 0
for i in range(1, 11):
    num = int(input(f"enter number {i}: "))
    if num % 2 == 0:
        even += 1
print("number of even is: ", even)