#Abegail Q. fernandez BSCPE1-4
#B6_Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter a string: ")
title_text = " ".join(word[:1].upper() + word[1:].lower() for word in text.split())
print(title_text)