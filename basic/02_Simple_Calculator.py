# Basic Python program to perform simple arithmetic operations (addition, subtraction, multiplication, division).
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    #we can also use int() instead of float() to take integer input

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")   #F-string is used to insert variables and expressions directly into a string using {}.
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")