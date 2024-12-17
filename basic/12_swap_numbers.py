# Program to swap two numbers without using a temporary variable
print("\n""Program to swap two numbers without using a temporary variable")     # \n is used to print a new blank line

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a

print(f"After swapping: First number = {a}, Second number = {b}")



# Program to swap two numbers using a temporary variable
print("\n""Program to swap two numbers using a temporary variable")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

temp = a
a = b
b = temp

print(f"After swapping: First number = {a}, Second number = {b}")
