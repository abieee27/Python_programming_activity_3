#Abegail Q. fernandez BSCPE1-4
#B2_Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

num = 0
for number in range (0, 101):
    while number % 2 != 0:
        print(number)
        break