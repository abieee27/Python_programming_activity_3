#Abegail Q. fernandez BSCPE1-4
#B1_Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

for num in range (0, 101):
    if num % 10 != 0:
        print(num)