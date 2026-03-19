#Abegail Q. fernandez BSCPE1-4
#B4_Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

nums = []
for i in range(10):
    n= int(input("enter a number: "))
    nums.append(n)
print("duplicate numbers: ")
found = False
for x in nums:
    if nums.count(x) > 1:
        if not x in nums[:nums.index(x)]:
            print(x)
            found = True
if not found:
    print("No duplicates found.")