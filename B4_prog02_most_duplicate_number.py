#Abegail Q. fernandez BSCPE1-4
#B4_Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

from collections import Counter

numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        num = float(input())
        numbers.append(num)
    except:
        break

if numbers:
    freq = Counter(numbers)
    most_common_num, count = freq.most_common(1)[0]
    
    print(f"Most frequent: {int(most_common_num) if most_common_num.is_integer() else most_common_num}")
    print(f"Count: {count}")