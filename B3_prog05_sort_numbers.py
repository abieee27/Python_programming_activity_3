#Abegail Q. fernandez BSCPE1-4
#B3_Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

numbers = []

while True:
    try:
        num = int(input("Enter number: "))
        numbers.append(num)
    except:
        break

numbers.sort()

for num in numbers:
    print(num)