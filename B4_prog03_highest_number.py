#Abegail Q. fernandez BSCPE1-4
#B4_Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

numbers = []
print("enter numbers (enter a non-numeric value to stop):")

while True:
    try:
        num = float(input())
        numbers.append(num)
    except:
        break
if numbers:
    highest = max(numbers)
    print(f"the highest number: {int(highest) if highest.is_integer() else highest}")
else:
    print("no numbers entered!")