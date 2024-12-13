# Basic Python program to check whether a number is prime.
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):     # the ** 0.5 is used to find the square root of the number
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")