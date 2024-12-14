# Program to check if a string or number is a palindrome or not.
text = input("Enter a string or number: ")

if text.isdigit():                   # Check if the input is a number
    print(f"Input is a number: {text}")
else:
    print(f"Input is a string: {text}")

if text == text[::-1]:                #syntax: string[start:end:step]     # [::-1] is used to reverse the string
                                      #Here, start and end are omitted (meaning the entire string is considered)
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")