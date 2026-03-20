#Abegail Q. fernandez BSCPE1-4
#B5_Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

num = input("enter a number(0,100): ")
num = int(num)
formatted_num = str(num).zfill(6)
print("output: ", formatted_num)
