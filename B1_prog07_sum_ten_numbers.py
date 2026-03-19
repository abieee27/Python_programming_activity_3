#abegail Q. fernandez BSCPE1-4
#B1_Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

total = 0
for i in range(1, 11):
     num = float(input(f"enter number {i}: "))
     total += num

print("the sum of all numbers is: ", total)