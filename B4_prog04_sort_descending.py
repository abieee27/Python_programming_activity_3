#Abegail Q. fernandez BSCPE1-4
#B4_Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# Program to collect numbers and display them from highest to lowest
numbers = []

print("Number Sorter (Highest to Lowest)")
print("Enter numbers (non-number input to stop):\n")

while True:
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
        numbers.append(num)
        
    except ValueError:
        print("\n Invalid input detected. Stopping...")
        break

if not numbers:
    print("No valid numbers were entered!")
else:
    numbers.sort(reverse=True)
    
    print("\n Numbers from HIGHEST to LOWEST ")
    for i, num in enumerate(numbers, 1):
        print(f"{i}. {int(num) if num.is_integer() else num}")
