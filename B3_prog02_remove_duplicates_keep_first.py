#Abegail Q. fernandez BSCPE1-4
#B3_Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []
seen = []
for i in range (1,11):
    num = int(input(f"enter number {i}: "))
    if num in range (1,11):
        numbers.append(num)

for num in numbers:
    if num not in seen:
      print(num)
      seen.append(num)
