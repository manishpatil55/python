# Program to check if an input character is a vowel or consonant
char = input("Enter a single alphabet: ").lower()

if char in "aeiou":
    print(f"'{char}' is a vowel.")
elif char.isalpha():
    print(f"'{char}' is a consonant.")
else:
    print("Invalid input. Please enter an alphabet.")