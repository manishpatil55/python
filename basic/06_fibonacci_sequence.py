# Basic Python program to generate Fibonacci sequence up to n terms.
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")

a, b = 0, 1

for i in range(n):
    print(a,end=" ")    #prints on the same line
#    print(a)            #prints on new line
    a, b = b, a + b