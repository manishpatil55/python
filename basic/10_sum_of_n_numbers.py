# Basic Python program to find the sum of the first n natural numbers.
n = int(input("Enter a number: "))
if n < 0:
    print("Enter a positive number.")
else:
    sum = n * (n + 1) // 2             # the "//" is used for rounding off the division result
    print(f"The sum of the first {n} natural numbers is {sum}.")