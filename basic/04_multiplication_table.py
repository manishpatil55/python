# Basic Python program to print the multiplication table of a given number.
num = int(input("Enter a number for the multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   #F-string is used to insert variables and expressions directly into a string using {}.