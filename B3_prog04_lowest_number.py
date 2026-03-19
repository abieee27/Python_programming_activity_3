#Abegail Q. fernandez BSCPE1-4
#B3_Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

numbers = []
while True:
    try:
        num = int(input("enter a number: "))
        numbers.append(num)
    except:
        break
print("lowest number: ", min(numbers))