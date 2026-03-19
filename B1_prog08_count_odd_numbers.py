#abegail Q. fernandez BSCPE1-4
#B1_Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_count = 0
for i in range (1, 11):
    num = float(input(f"enter number {i}: "))
    if num % 2!= 0:
        odd_count +=1
print("the number of odd numbers are: ", odd_count)