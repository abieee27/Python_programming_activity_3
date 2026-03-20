#Abegail Q. fernandez BSCPE1-4
#B4_Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

total = 0
count = 0

while True:
    user_input = input("enter a number: ")
    
    if not user_input.replace('.','',1).isdigit():
        break
    num = float(user_input)
    total += num
    count +=1

if count > 0:
    average = total / count
    print("the average is:", average)
else:
    print("no valid numbers entered,")
