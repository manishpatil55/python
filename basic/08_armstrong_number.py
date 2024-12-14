# Program to check if a number is an Armstrong number

num = int(input("Enter a number: "))
temp = num                                # Copy the number to a temporary variable
sum = 0                                   # Initialize the sum to 0
num_digits = len(str(num))                # Calculate the number of digits in the number
while temp > 0:
    digit = temp % 10               # Extract the last digit
    sum += digit ** num_digits      # add the power of the digit to the sum
    temp //= 10                     # Remove the last digit

if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")